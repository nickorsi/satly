SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

-- Clean out existing table data cleanly
DROP TABLE IF EXISTS public.photos CASCADE;
DROP SEQUENCE IF EXISTS public.photos_id_seq CASCADE;

-- Recreate the table structure
CREATE TABLE public.photos (
    id integer NOT NULL,
    title character varying(300) NOT NULL,
    caption character varying(700) NOT NULL,
    s3_photo_url_orig character varying(700) NOT NULL,
    s3_photo_url_display character varying(700) NOT NULL,
    edited boolean NOT NULL,
    black_and_white boolean NOT NULL,
    active boolean NOT NULL
);

CREATE SEQUENCE public.photos_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER SEQUENCE public.photos_id_seq OWNED BY public.photos.id;
ALTER TABLE ONLY public.photos ALTER COLUMN id SET DEFAULT nextval('public.photos_id_seq'::regclass);
ALTER TABLE ONLY public.photos ADD CONSTRAINT photos_pkey PRIMARY KEY (id);

-- Standard SQL Insert statements safe for SQLAlchemy execution
INSERT INTO public.photos (id, title, caption, s3_photo_url_orig, s3_photo_url_display, edited, black_and_white, active) VALUES
(2, 'Classic Mortons', 'Can''t beat the classic.', 'https://saltly-bucket.s3.us-west-1.amazonaws.com/mortons.jpeg', 'https://saltly-bucket.s3.us-west-1.amazonaws.com/display_mortons.jpeg', false, false, true),
(1, 'Bag O Salt', 'Magical Salt', 'https://saltly-bucket.s3.us-west-1.amazonaws.com/bag-o-salt.jpeg', 'https://saltly-bucket.s3.us-west-1.amazonaws.com/display_bag-o-salt.jpeg', true, true, true),
(3, 'The King of Salt', 'Salt bae forever.', 'https://saltly-bucket.s3.us-west-1.amazonaws.com/salt-bae.jpeg', 'https://saltly-bucket.s3.us-west-1.amazonaws.com/display_salt-bae.jpeg', false, false, true),
(4, 'O Magical Bowl O Salt', 'Salt Bowl', 'https://saltly-bucket.s3.us-west-1.amazonaws.com/salt-bowl.jpeg', 'https://saltly-bucket.s3.us-west-1.amazonaws.com/display_salt-bowl.jpeg', false, false, true),
(5, 'Salt Flats', 'So beautiful', 'https://saltly-bucket.s3.us-west-1.amazonaws.com/salt-flat.jpeg', 'https://saltly-bucket.s3.us-west-1.amazonaws.com/display_salt-flat.jpeg', false, false, true),
(6, 'Salt Grain', 'So many salts!', 'https://saltly-bucket.s3.us-west-1.amazonaws.com/salt-grain.jpeg', 'https://saltly-bucket.s3.us-west-1.amazonaws.com/display_salt-grain.jpeg', false, false, true),
(7, 'Lake of Salt', 'Don''t drink that water!', 'https://saltly-bucket.s3.us-west-1.amazonaws.com/salt-lake.jpeg', 'https://saltly-bucket.s3.us-west-1.amazonaws.com/display_salt-lake.jpeg', false, false, true),
(8, 'Salt Lamp', 'Sooooo soothing', 'https://saltly-bucket.s3.us-west-1.amazonaws.com/salt-lamp.jpeg', 'https://saltly-bucket.s3.us-west-1.amazonaws.com/display_salt-lamp.jpeg', false, false, true),
(9, 'Salt Piles', 'Salt never ending', 'https://saltly-bucket.s3.us-west-1.amazonaws.com/salt-piles-more.jpeg', 'https://saltly-bucket.s3.us-west-1.amazonaws.com/display_salt-piles-more.jpeg', false, false, true),
(10, 'Salt salt salt', 'So much salt', 'https://saltly-bucket.s3.us-west-1.amazonaws.com/salt-piles.jpeg', 'https://saltly-bucket.s3.us-west-1.amazonaws.com/display_salt-piles.jpeg', false, false, true),
(11, 'Praise the salt', 'Praise the salt', 'https://saltly-bucket.s3.us-west-1.amazonaws.com/salt-pyramid.jpeg', 'https://saltly-bucket.s3.us-west-1.amazonaws.com/display_salt-pyramid.jpeg', false, false, true),
(12, 'Salt Spoon', 'Just a spoonful please!', 'https://saltly-bucket.s3.us-west-1.amazonaws.com/salt-spoon.jpeg', 'https://saltly-bucket.s3.us-west-1.amazonaws.com/display_salt-spoon.jpeg', false, false, true),
(13, 'Salt Fight', 'Getting salty in here', 'https://saltly-bucket.s3.us-west-1.amazonaws.com/salt-sumo.jpeg', 'https://saltly-bucket.s3.us-west-1.amazonaws.com/display_salt-sumo.jpeg', false, false, true),
(14, 'Salts', 'Salts pure and simple', 'https://saltly-bucket.s3.us-west-1.amazonaws.com/salts.jpeg', 'https://saltly-bucket.s3.us-west-1.amazonaws.com/display_salts.jpeg', false, false, true),
(15, 'Salty', 'Too much salt', 'https://saltly-bucket.s3.us-west-1.amazonaws.com/salty-salty.jpeg', 'https://saltly-bucket.s3.us-west-1.amazonaws.com/display_salty-salty.jpeg', false, false, true),
(16, 'Salty salty', 'Too salty', 'https://saltly-bucket.s3.us-west-1.amazonaws.com/salty.jpeg', 'https://saltly-bucket.s3.us-west-1.amazonaws.com/display_salty.jpeg', false, false, true);

-- Fix sequence counter to match the max id (16)
SELECT pg_catalog.setval('public.photos_id_seq', 16, true);