import logging
logging.basicConfig(level=logging.DEBUG)

import unittest

import requests

from snortparser import parse_rules


LOG = logging.getLogger(__name__)


RULESET_URLS = [
    'https://rules.emergingthreats.net/open/snort-2.9.0/rules/emerging-activex.rules',
    'https://rules.emergingthreats.net/open/snort-2.9.0/rules/emerging-attack_response.rules',
    'https://rules.emergingthreats.net/open/snort-2.9.0/rules/emerging-botcc.portgrouped.rules',
    'https://rules.emergingthreats.net/open/snort-2.9.0/rules/emerging-malware.rules',
    'https://rules.emergingthreats.net/open/snort-2.9.0/rules/emerging-web_specific_apps.rules',
    'https://rules.emergingthreats.net/open/snort-2.9.0/rules/emerging-trojan.rules'
]

class OSINTTest(unittest.TestCase):
    def osint_test(self):
        for url in RULESET_URLS:
            LOG.info('parsing {}'.format(url))

            ruleset = requests.get(url, stream=True)
            ruleset.raise_for_status()

            rulen = None
            for rulen, rule in enumerate(parse_rules(ruleset.iter_lines())):
                for o in rule.tokenize_opts():
                    pass

            self.assertNotEqual(rulen, None)
            LOG.info('{} - parsed {} rules'.format(url, rulen))
