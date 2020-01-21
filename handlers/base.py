import hashlib
import aiohttp_jinja2
import json

from aiohttp import web
from aiohttp_session import get_session
from config.common import BaseConfig


from models.user import User


class Index(web.View):

    @aiohttp_jinja2.template('base.html')
    async def get(self):
        conf = self.app['config']
        session = await get_session(self)
        user = {}
        if 'user' in session:
            user_id = session['user']
            user = await User.get_user_by_id(self.app['db'], user_id)
        return dict(user=user, conf=conf)

class Login(web.View):

    @aiohttp_jinja2.template('login.html')
    async def get(self):
        session = await get_session(self)
        user = {}
        conf = self.app['config']
        if 'user' in session:
            user = session['user']
            return dict(user = user, conf= conf)
        return dict(user = user, conf=conf)

    async def post(self):
        data = await self.post()
        session = await get_session(self)
        location = self.app.router['login'].url_for()
        email = data['email']
        password = data['password']
        user = await User.get_user_by_email(self.app['db'], email)
        print(user)
        if str(user['password']) == password:
            session['user'] = user['id']

            location = self.app.router['index'].url_for()

            return web.HTTPFound(location=location)

        return web.HTTPFound(location=location)


class Signup:

    @aiohttp_jinja2.template('sigup.html')
    async def get(self):
        session = await get_session(self)
        user = {}
        if 'user' in session:
            user = session['user']
        return dict(user=user)

    async def post(self):
        data = await self.post()
        location = self.app.router['signup'].url_for()

        email = data['email']
        name = data['name']
        secondname = data['secondname']
        birthday = data['date']
        phone = data['phone']
        occupation = data['occupation']
        city = data['city']
        password = data['password']
        
        user_by_email = await User.get_user_by_email(self.app['db'], email)
        if user_by_email:
            return web.HTTPFound(location = location)

        if name and secondname and birthday and phone and occupation and city and password:
            data = dict(data)
            data['password'] = hashlib.sha256(data['password'].encode('utf-8')).hexdigest()
            password = data['password']

            result = await User.create_user(self.app['db'], email, name, secondname, birthday, int(phone), occupation, city, password)
            location = self.app.router['login'].url_for()
            return web.HTTPFound(location=location)
        else:
            return dict(error='Missing user data parameters')

        


class Logout:

    async def get(self):
        session = await get_session(self)
        try:
            del session['user']
        except:
            pass
        location = self.app.router['index'].url_for()

        return web.HTTPFound(location = location)


class Profile:
    
    @aiohttp_jinja2.template('lk.html')
    async def get(self):
        session = await get_session(self)
        config = self.app['config']
        user = {}
        if 'user' in session:
            user_id = session['user']
            user = await User.get_user_by_id(self.app['db'], user_id)
        return dict(config=config, user=user)

class UserProjects:

    @aiohttp_jinja2.template('myprojects.html')
    async def get(self):
        session = await get_session(self)
        config = self.app['config']
        user = {}
        if 'user' in session:
            user_id = session['user']
            user = await User.get_user_by_id(self.app['db'], user_id)
        return dict(config=config, user=user)
    
    async def post(self):
        pass

class Projects:

    @aiohttp_jinja2.template('projects.html')
    async def get(self):
        session = await get_session(self)
        config = self.app['config']
        user = {}
        if 'user' in session:
            user_id = session['user']
            user = await User.get_user_by_id(self.app['db'], user_id)
        return dict(config=config, user=user)

class About:

    @aiohttp_jinja2.template('about_site.html')
    async def get(self):
        session = await get_session(self)
        config = self.app['config']
        user = {}
        if 'user' in session:
            user_id = session['user']
            user = await User.get_user_by_id(self.app['db'], user_id)
        return dict(config=config, user=user)


class Contacts:

    @aiohttp_jinja2.template('contact.html')
    async def get(self):
        session = await get_session(self)
        config = self.app['db']
        user = {}
        if 'user' in session:
            user_id = session['user']
            user = await User.get_user_by_id(self.app['db'], user_id)
        return dict(config=config, user=user)

