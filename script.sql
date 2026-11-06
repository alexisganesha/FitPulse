-- 1. DROP TABLES (dans l'ordre inverse des clés étrangères)
DROP TABLE IF EXISTS public.training;
DROP TABLE IF EXISTS public.users;
DROP TABLE IF EXISTS public.subscription;
DROP TABLE IF EXISTS public.followcourse;

-- 2. CREATE TABLES
CREATE TABLE public.subscription
(
    id serial NOT NULL,
    type character varying(100) COLLATE pg_catalog."default" NOT NULL,
    prix money,
    duree integer,
    CONSTRAINT subscription_pkey PRIMARY KEY (id)
)
TABLESPACE pg_default;

ALTER TABLE public.subscription OWNER to postgres;

CREATE TABLE public.users
(
    id serial NOT NULL,
    email character varying(255) COLLATE pg_catalog."default" NOT NULL,
    last_name character varying(100) COLLATE pg_catalog."default",
    role character varying(50) COLLATE pg_catalog."default",
    abo integer,
    CONSTRAINT users_pkey PRIMARY KEY (id)
)
TABLESPACE pg_default;

ALTER TABLE public.users OWNER to postgres;

CREATE TABLE public.training
(
    id serial NOT NULL,
    description character varying(255) COLLATE pg_catalog."default" NOT NULL,
    hour_start time without time zone NOT NULL,
    hour_end time without time zone NOT NULL,
    day integer NOT NULL,
    user_id integer,
    CONSTRAINT training_pkey PRIMARY KEY (id),
    CONSTRAINT fk_user FOREIGN KEY (user_id)
        REFERENCES public.users (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE SET NULL
)
TABLESPACE pg_default;

ALTER TABLE public.training OWNER to postgres;

-- 3. INSERT INTO DATA
INSERT INTO public.subscription (id, type, prix, duree) VALUES
(1, 'ultimate', '34.99'::numeric::money, 56),
(2, 'premium', '29.99'::numeric::money, 46),
(3, 'comfort', '24.99'::numeric::money, 46),
(5, 'eaezaez', '26.00'::numeric::money, 10);

INSERT INTO public.users (id, email, last_name, role, abo) VALUES
(1, 'alexis@supersport.com', 'Alexis', 'admin', 1),
(2, 'tibo_in_shape@supersport.com', 'Tibo', 'user', 1),
(3, 'damien_motive@supersport.com', 'Damien', 'user', 2),
(4, 'amandine@supersport.com', 'Amandine', 'user', 3),
(5, 'alex.j@fitpulse.com', 'Johnson', 'trainer', 1),
(6, 'sarah.c@fitpulse.com', 'Connor', 'trainer', 1),
(7, 'david.b@fitpulse.com', 'Belle', 'trainer', 1),
(8, 'emma.w@fitpulse.com', 'Watson', 'trainer', 1),
(9, 'lucas.s@fitpulse.com', 'Scott', 'trainer', 1);

INSERT INTO public.training (id, description, hour_start, hour_end, day, user_id) VALUES
(1, 'HIIT Cardio', '12:00:00', '13:00:00', 1, 1),
(2, 'Power Yoga', '18:30:00', '19:30:00', 1, 4),
(3, 'Spinning / Indoor Cycling', '08:00:00', '09:00:00', 2, 2),
(4, 'BodyPump', '19:00:00', '20:15:00', 2, 5),
(5, 'Crossfit WOD', '10:00:00', '11:30:00', 3, 2),
(6, 'Pilates Matwork', '17:00:00', '18:00:00', 3, 4),
(7, 'Zumba Fitness', '19:30:00', '20:30:00', 3, 1),
(8, 'LesMills BodyCombat', '12:15:00', '13:15:00', 4, 5),
(9, 'Stretching & Mobility', '16:00:00', '17:00:00', 4, 4),
(10, 'Boxing Conditioning', '18:00:00', '19:30:00', 5, 2),
(11, 'Core & Abs Blast', '12:30:00', '13:00:00', 5, 2),
(12, 'Aquagym', '09:30:00', '10:30:00', 6, 1),
(13, 'Barre Fitness', '11:00:00', '12:00:00', 6, 4),
(14, 'Strongman Introduction', '14:00:00', '16:00:00', 6, 1),
(15, 'Sunday FullBody Workout', '10:30:00', '12:00:00', 7, 5),
(16, 'aeaez', '12:00:00', '13:00:00', 1, 5);

-- 4. Synchronisation des compteurs d'auto-incrément (Séquences serial)
SELECT setval('public.subscription_id_seq', COALESCE((SELECT MAX(id)+1 FROM public.subscription), 1), false);
SELECT setval('public.users_id_seq', COALESCE((SELECT MAX(id)+1 FROM public.users), 1), false);
SELECT setval('public.training_id_seq', COALESCE((SELECT MAX(id)+1 FROM public.training), 1), false);


CREATE TABLE IF NOT EXISTS public.followcourse
(
    user_id integer NOT NULL,
    training_id integer NOT NULL,
    date_inscription timestamp without time zone DEFAULT CURRENT_TIMESTAMP, -- Optionnel : pour savoir quand ils se sont inscrits
    
    -- La clé primaire composée empêche un utilisateur de s'inscrire deux fois au même cours
    CONSTRAINT followcourse_pkey PRIMARY KEY (user_id, training_id), 
    
    -- Clés étrangères pour l'intégrité des données
    CONSTRAINT fk_follow_user FOREIGN KEY (user_id)
        REFERENCES public.users (id) ON DELETE CASCADE,
    CONSTRAINT fk_follow_training FOREIGN KEY (training_id)
        REFERENCES public.training (id) ON DELETE CASCADE
)
TABLESPACE pg_default;

ALTER TABLE public.followcourse OWNER to postgres;