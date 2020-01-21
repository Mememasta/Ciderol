
Drop table projects_user;

Drop table projects;

Drop table message;

Drop table users;

Drop table groups;



create table groups (
        id serial primary key,
        name varchar(255)
        
);

create table users (
        id serial primary key,
        name varchar(255),
        secondname varchar(255),
        email varchar(255),
        phone integer,
        birthday VARCHAR(40),
        occupation varchar(255),
        city varchar(40),
        groups_id integer references groups(id),
        password VARCHAR(255),
        user_photo text

);

create table message (
        id serial primary key,
        from_id integer references users(id),
        to_id integer references users(id),
        text text,
        photo text
);

create table projects (
        id serial primary key,
        name text,
        company text,
        author_id integer references users(id),
        presentation VARCHAR(255),
        deadline VARCHAR(255),
        gift text,
        video VARCHAR(255)
);

create table projects_user (
        user_id integer references users(id),
        project_id integer references projects(id)

);

insert into groups (name) values ('Yandex');

insert into users (name, secondname, email, phone, birthday, occupation, city, groups_id, password, user_photo) values ('Nikita', 'Russkih', 'test@gmail.com', 8888, '1999-10-22', 'student', 'SPB', 1, '123', '/static/user_photo/nikita.jpg');


insert into users (name, secondname, email, phone, birthday, occupation, city, groups_id, password, user_photo) values ('Marat', 'Chuchalov', 'morat@gmail.com', 8909, '1998-10-05', 'student', 'Izh', 1, '0912', '/static/user_photo/marat.jpg');


insert into message (from_id, to_id, text, photo) values (1, 2, 'Привет', '/static/photo/1.jpg');


insert into message (from_id, to_id, text, photo) values (2, 1, 'Хай', '');

insert into projects (name, company, author_id, presentation, deadline, gift, video) values ('Нейросеть для шахты', 'Горный', 1, '/static/files/mining.pdf', '2020-01-10', 'Поступление в университет', '/static/video/mining.mp4');

insert into projects_user (user_id, project_id) values (2, 1);


insert into projects_user (user_id, project_id) values (1, 1);
