--
-- PostgreSQL database dump
--

-- Dumped from database version 14.10 (Ubuntu 14.10-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 14.10 (Ubuntu 14.10-0ubuntu0.22.04.1)
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
4	Single grain of salt	Just the one grain	https://saltly.s3.us-west-1.amazonaws.com/single-grain-of-salt.jpg	https://saltly.s3.us-west-1.amazonaws.com/display_single-grain-of-salt.jpg	f	f	t
5	Tainted salt	Do not eat	https://saltly.s3.us-west-1.amazonaws.com/tainted-salt.jpg	https://saltly.s3.us-west-1.amazonaws.com/display_tainted-salt.jpg	f	f	t
6	Even more too much salt	Too much of a good thing, taken to an extreme	https://saltly.s3.us-west-1.amazonaws.com/even-more-too-much-salt.jpg	https://saltly.s3.us-west-1.amazonaws.com/display_even-more-too-much-salt.jpg	f	f	t
7	Salt on egg	Put some salt on an egg if you want to	https://saltly.s3.us-west-1.amazonaws.com/salt-egg.jpg	https://saltly.s3.us-west-1.amazonaws.com/display_salt-egg.jpg	f	f	t
8	Saltamids	Bury a salty pharaoh in the salt	https://saltly.s3.us-west-1.amazonaws.com/saltamid.jpg	https://saltly.s3.us-west-1.amazonaws.com/display_saltamid.jpg	f	f	t
9	Hand salt	Hand with salt	https://saltly.s3.us-west-1.amazonaws.com/hand-salt.jpg	https://saltly.s3.us-west-1.amazonaws.com/display_hand-salt.jpg	f	f	t
10	Salt mine	Where does all the salt come from? Here.	https://saltly.s3.us-west-1.amazonaws.com/salt-mine.jpg	https://saltly.s3.us-west-1.amazonaws.com/display_salt-mine.jpg	f	f	t
11	A guy that loves salt	Pray to the salty god of salt that is itself salt	https://saltly.s3.us-west-1.amazonaws.com/marco-and-salt.jpg	https://saltly.s3.us-west-1.amazonaws.com/display_marco-and-salt.jpg	f	f	t
12	Pink salt	Salt that is pink	https://saltly.s3.us-west-1.amazonaws.com/pink-salt.jpg	https://saltly.s3.us-west-1.amazonaws.com/display_pink-salt.jpg	f	f	t
13	Field of salt	Soccer (also known as football to most Europeans) is not allowed here	https://saltly.s3.us-west-1.amazonaws.com/flat-salt.jpg	https://saltly.s3.us-west-1.amazonaws.com/display_flat-salt.jpg	f	f	t
14	Salt and friends	Look, salt has invited its friends over for a spoon party	https://saltly.s3.us-west-1.amazonaws.com/salt-and-friends.jpg	https://saltly.s3.us-west-1.amazonaws.com/display_salt-and-friends.jpg	f	f	t
3	Peruvian salt mines	Look at these salt mines.	https://saltly.s3.us-west-1.amazonaws.com/jeff-anders-C3nd17u38kg-unsplash.jpg	https://saltly.s3.us-west-1.amazonaws.com/display_jeff-anders-C3nd17u38kg-unsplash.jpg	t	t	t
15	Salt Surface	Some surfaces are salted, including this one	https://saltly.s3.us-west-1.amazonaws.com/salted-surface.jpg	https://saltly.s3.us-west-1.amazonaws.com/display_salted-surface.jpg	f	f	t
16	Octopus	All of this being's arms are salty because of its environment	https://saltly.s3.us-west-1.amazonaws.com/drawasaurus-octopus.png	https://saltly.s3.us-west-1.amazonaws.com/display_drawasaurus-octopus.png	f	f	t
17	Too much salt	Wow, I'm overwhelmed	https://saltly.s3.us-west-1.amazonaws.com/too-much-salt.jpg	https://saltly.s3.us-west-1.amazonaws.com/display_too-much-salt.jpg	f	f	t
20	Salt bowl	If you need some salt, you can get some from this bowl by asking your next door neighbor even though he's kinda aloof	https://saltly.s3.us-west-1.amazonaws.com/faran-raufi-u_Mwofs_zu0-unsplash.jpg	https://saltly.s3.us-west-1.amazonaws.com/display_faran-raufi-u_Mwofs_zu0-unsplash.jpg	f	f	t
\.


--
-- Name: photos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.photos_id_seq', 24, true);


--
-- Name: photos photos_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.photos
    ADD CONSTRAINT photos_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

