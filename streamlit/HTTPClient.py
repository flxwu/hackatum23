import aiohttp
import asyncio
import logging
import contextlib
from http.client import HTTPConnection
import aiohttp


def debug_requests_on():
    '''Switches on logging of the requests module.'''
    HTTPConnection.debuglevel = 1

    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True


def debug_requests_off():
    '''Switches off logging of the requests module, might be some side-effects'''
    HTTPConnection.debuglevel = 0

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.WARNING)
    root_logger.handlers = []
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.WARNING)
    requests_log.propagate = False


@contextlib.contextmanager
def debug_requests():
    '''Use with 'with'!'''
    debug_requests_on()
    yield
    debug_requests_off()


url_post = "https://api.deepinfra.com/v1/inference/meta-llama/Llama-2-7b-chat-hf"


async def post(body, session):
    try:
        async with session.post(url_post, json=body) as resp:
            return await resp.json()
    except Exception as e:
        print("Unable to get url {} due to {}.".format(url_post, e.__class__))


async def parallel_post(payloads):
    async with aiohttp.ClientSession() as session:
        reqs = []
        for i, p in enumerate(payloads):
            reqs.append(post(p, session))
            print(f"[LOGLENS] POST Request {i} fired")

        ret = await asyncio.gather(*reqs)
        print(
            "[LOGLENS] Finalized all. Return is a list of len {} outputs.".format(len(ret)))
        return ret
