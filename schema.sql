drop table if exists posts;
create table posts( id integer PRIMARY key,
	name text not null,
	content text not null );