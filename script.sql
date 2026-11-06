-- 1. DROP TABLES (dans l'ordre inverse des clés étrangères)
DROP TABLE IF EXISTS public.followcourse CASCADE;
DROP TABLE IF EXISTS public.training CASCADE;
DROP TABLE IF EXISTS public.users CASCADE;
DROP TABLE IF EXISTS public.subscription CASCADE;

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

-- 3. INSERT INTO DATA
INSERT INTO public.subscription (id, type, prix, duree) VALUES
(1, 'ultimate', '34.99'::numeric::money, 56),
(2, 'premium', '29.99'::numeric::money, 46),
(3, 'comfort', '24.99'::numeric::money, 46),
(5, 'eaezaez', '26.00'::numeric::money, 10);

INSERT INTO public.users (id, email, last_name, role, abo) VALUES
(1, 'alexis@fitpulse.com', 'Alexis', 'admin', 1),
(2, 'tibo_in_shape@fitpulse.com', 'Tibo', 'trainer', 1),
(3, 'damien_motive@fitpulse.com', 'Damien', 'user', 2),
(4, 'amandine@fitpulse.com', 'Amandine', 'user', 3),
(5, 'alex.j@fitpulse.com', 'Johnson', 'trainer', 1),
(6, 'sarah.c@fitpulse.com', 'Connor', 'trainer', 1),
(7, 'david.b@fitpulse.com', 'Belle', 'trainer', 1),
(8, 'emma.w@fitpulse.com', 'Watson', 'trainer', 1),
(9, 'lucas.s@fitpulse.com', 'Scott', 'trainer', 1),
(10, 'marc.durand@fitpulse.com', 'Marc', 'user', 2),
(11, 'sophie.lefevre@fitpulse.com', 'Sophie', 'user', 1),
(12, 'thomas.dubois@fitpulse.com', 'Thomas', 'user', 3),
(13, 'julie.moreau@fitpulse.com', 'Julie', 'user', 2),
(14, 'nicolas.roux@fitpulse.com', 'Nicolas', 'user', 1);

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



-- Table: followcourse (10 Inscriptions générées)
INSERT INTO public.followcourse (user_id, training_id) VALUES
(1, 3),   -- Alexis (admin) suit le Spinning
(3, 1),   -- Damien (user) suit le HIIT Cardio
(3, 5),   -- Damien (user) suit le Crossfit
(4, 2),   -- Amandine (user) suit le Power Yoga
(10, 4),  -- Marc (user) suit le BodyPump
(10, 8),  -- Marc (user) suit le BodyCombat
(11, 6),  -- Sophie (user) suit le Pilates
(12, 1),  -- Thomas (user) suit le HIIT Cardio
(13, 7),  -- Julie (user) suit la Zumba
(14, 15); -- Nicolas (user) suit le Sunday FullBody Workout

-- ============================================================================
-- 4. SYNCHRONISATION DES COMPTEURS D'AUTO-INCREMENT (Séquences serial)
-- ============================================================================
SELECT setval('public.subscription_id_seq', COALESCE((SELECT MAX(id)+1 FROM public.subscription), 1), false);
SELECT setval('public.users_id_seq', COALESCE((SELECT MAX(id)+1 FROM public.users), 1), false);
SELECT setval('public.training_id_seq', COALESCE((SELECT MAX(id)+1 FROM public.training), 1), false);



