from os import environ as env
from dotenv import load_dotenv

load_dotenv()

print('CLIENT_ID:  {}'.format(env['CLIENT_ID']))
print('CLIENT_SECRET: {}'.format(env['CLIENT_SECRET']))
print('USER_AGENT:     {}'.format(env['USER_AGENT']))
