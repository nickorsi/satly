--
-- PostgreSQL database dump
--

-- Dumped from database version 15.4 (Homebrew)
-- Dumped by pg_dump version 15.4 (Homebrew)

DROP DATABASE IF EXISTS  saltly;
CREATE DATABASE saltly;

\c saltly

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

ALTER TABLE ONLY public.photos DROP CONSTRAINT photos_pkey;
ALTER TABLE public.photos ALTER COLUMN id DROP DEFAULT;
DROP SEQUENCE public.photos_id_seq;
DROP TABLE public.photos;
SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: photos; Type: TABLE; Schema: public; Owner: -
--

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


--
-- Name: photos_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.photos_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: photos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.photos_id_seq OWNED BY public.photos.id;


--
-- Name: photos id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.photos ALTER COLUMN id SET DEFAULT nextval('public.photos_id_seq'::regclass);


--
-- Data for Name: photos; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.photos (id, title, caption, s3_photo_url_orig, s3_photo_url_display, edited, black_and_white, active) FROM stdin;
2	Classic Mortons	Can't beat the classic. 	https://saltly-bucket.s3.us-west-1.amazonaws.com/mortons.jpeg	https://saltly-bucket.s3.us-west-1.amazonaws.com/display_mortons.jpeg	f	f	t
1	Bag O Salt	Magical Salt	https://saltly-bucket.s3.us-west-1.amazonaws.com/bag-o-salt.jpeg	https://saltly-bucket.s3.us-west-1.amazonaws.com/display_bag-o-salt.jpeg	t	t	t
3	The King of Salt	Salt bae forever.	https://saltly-bucket.s3.us-west-1.amazonaws.com/salt-bae.jpeg	https://saltly-bucket.s3.us-west-1.amazonaws.com/display_salt-bae.jpeg	f	f	t
4	O Magical Bowl O Salt	Salt Bowl	https://saltly-bucket.s3.us-west-1.amazonaws.com/salt-bowl.jpeg	https://saltly-bucket.s3.us-west-1.amazonaws.com/display_salt-bowl.jpeg	f	f	t
5	Salt Flats	So beautiful	https://saltly-bucket.s3.us-west-1.amazonaws.com/salt-flat.jpeg	https://saltly-bucket.s3.us-west-1.amazonaws.com/display_salt-flat.jpeg	f	f	t
6	Salt Grain	So many salts!	https://saltly-bucket.s3.us-west-1.amazonaws.com/salt-grain.jpeg	https://saltly-bucket.s3.us-west-1.amazonaws.com/display_salt-grain.jpeg	f	f	t
7	Lake of Salt	Don't drink that water!	https://saltly-bucket.s3.us-west-1.amazonaws.com/salt-lake.jpeg	https://saltly-bucket.s3.us-west-1.amazonaws.com/display_salt-lake.jpeg	f	f	t
8	Salt Lamp	Sooooo soothing	https://saltly-bucket.s3.us-west-1.amazonaws.com/salt-lamp.jpeg	https://saltly-bucket.s3.us-west-1.amazonaws.com/display_salt-lamp.jpeg	f	f	t
9	Salt Piles	Salt never ending	https://saltly-bucket.s3.us-west-1.amazonaws.com/salt-piles-more.jpeg	https://saltly-bucket.s3.us-west-1.amazonaws.com/display_salt-piles-more.jpeg	f	f	t
10	Salt salt salt	So much salt	https://saltly-bucket.s3.us-west-1.amazonaws.com/salt-piles.jpeg	https://saltly-bucket.s3.us-west-1.amazonaws.com/display_salt-piles.jpeg	f	f	t
11	Praise the salt	Praise the salt	https://saltly-bucket.s3.us-west-1.amazonaws.com/salt-pyramid.jpeg	https://saltly-bucket.s3.us-west-1.amazonaws.com/display_salt-pyramid.jpeg	f	f	t
12	Salt Spoon	Just a spoonful please!	https://saltly-bucket.s3.us-west-1.amazonaws.com/salt-spoon.jpeg	https://saltly-bucket.s3.us-west-1.amazonaws.com/display_salt-spoon.jpeg	f	f	t
13	Salt Fight	Getting salty in here	https://saltly-bucket.s3.us-west-1.amazonaws.com/salt-sumo.jpeg	https://saltly-bucket.s3.us-west-1.amazonaws.com/display_salt-sumo.jpeg	f	f	t
14	Salts	Salts pure and simple	https://saltly-bucket.s3.us-west-1.amazonaws.com/salts.jpeg	https://saltly-bucket.s3.us-west-1.amazonaws.com/display_salts.jpeg	f	f	t
15	Salty	Too much salt	https://saltly-bucket.s3.us-west-1.amazonaws.com/salty-salty.jpeg	https://saltly-bucket.s3.us-west-1.amazonaws.com/display_salty-salty.jpeg	f	f	t
16	Salty salty	Too salty	https://saltly-bucket.s3.us-west-1.amazonaws.com/salty.jpeg	https://saltly-bucket.s3.us-west-1.amazonaws.com/display_salty.jpeg	f	f	t
\.


--
-- Name: photos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.photos_id_seq', 16, true);


--
-- Name: photos photos_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.photos
    ADD CONSTRAINT photos_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

