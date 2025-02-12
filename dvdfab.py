import requests

from pick import pick

EDS_PRODUCTS = {
    'DVDFab': {
        'eds_pid': 20021,
        'software': {
            'win': {
                'DVDFab x86': '22,42,57,66',
                'DVDFab x64': '26,44,58,67'
            },
            'mac': {
                'DVDFab for Intel Chip': '41,56,65',
                'DVDFab for Apple Chip': '60,68'
            }
        }
    },
    'StreamFab': {
        'eds_pid': 20022,
        'software': {
            'win': {
                'StreamFab x86': '48',
                'StreamFab x64': '49'
            },
            'mac': {
                'StreamFab for Intel Chip': '50',
                'StreamFab for Apple Chip': '59'
            }
        }
    },
    'MusicFab': {
        'eds_pid': 20300,
        'software': {
            'win': {
                'MusicFab x86': '69',
                'MusicFab x64': '70'
            },
            'mac': {
                'MusicFab for Intel Chip': '71',
                'MusicFab for Apple Chip': '72'
            }
        }
    },
    'PlayerFab': {
        'eds_pid': 20024,
        'software': {
            'win': {
                'PlayerFab x86': '31',
                'PlayerFab x64': '12',
                'Player 6 x86': 'player6_31',
                'Player 6 x64': 'player6_12'
            },
            'mac': {
                'Player 6': '32',
                'Player 5': '28'
            }
        }
    },
    'UniFab': {
        'eds_pid': 20023,
        'software': {
            'win': {
                'UniFab x86': '98',
                'UniFab x64': '99',
                'Toolkit': '202',
                'Video Converter Pro': '93',
                'VideoCruise': '1051'
            },
            'mac': {
                'UniFab for Intel Chip': '100',
                'UniFab for Apple Chip': '104'
            }
        }
    },
    'Passkey': {
        'eds_pid': 20025,
        'software': {
            'win': {
                'Passkey': '20'
            }
        }
    },
    'Photo Enhancer AI': {
        'eds_pid': 20026,
        'software': {
            'win': {
                'Photo Enhancer AI': '90'
            }
        }
    },
    'Video Enhancer AI': {
        'eds_pid': 20027,
        'software': {
            'win': {
                'Video Enhancer AI': '92'
            }
        }
    },
    'Media Recover': {
        'eds_pid': 20028,
        'software': {
            'win': {
                'Media Recover': '91'
            }
        }
    },
    'Geekit': {
        'eds_pid': 20029,
        'software': {
            'win': {
                'Geekit': '25'
            }
        }
    },
    'ExplorerFab': {
        'eds_pid': None,
        'software': {
            'win': {
                'ExplorerFab x86': '203',
                'ExplorerFab x64': '204'
            }
        }
    }
}

if __name__ == '__main__':
    print('[*] Extended Download Service')

    try:
        name, _ = pick([k for k in EDS_PRODUCTS.keys()], 'Product')
        product = EDS_PRODUCTS[name]
        print('[+] Product:', name)
        platform, _ = pick([k for k in product['software'].keys()], 'Product')
        print('[+] Product:', platform)
        software, _ = pick([k for k in product['software'][platform].keys()], 'Software')
        print('[+] Software:', software)

        r = requests.request(
            method='GET',
            url='https://web-backend-us.dvdfab.cn/change_log/extend_download',
            params={
                'lang': 'en',
                'software': product['software'][platform][software]
            },
            headers={
                'Accept': 'application/json',
                'Accept-Encoding': 'gzip, deflate, br, zstd',
                'Accept-Language': 'en-US,en;q=0.9',
                'Connection': 'keep-alive',
                'Host': 'web-backend-us.dvdfab.cn',
                'Origin': 'https://www.dvdfab.cn',
                'Referer': 'https://www.dvdfab.cn/',
                'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
            }
        )
        r.raise_for_status()
        versions = r.json()['data']

        if versions:
            version, index = pick([v['version'] for v in versions], 'Version')
            print('[+] Version:', version)
            source = versions[index]['extend_download']
            print('[+] Download:', source)
        else:
            print('[!] No version available for this product')
    except Exception as e:
        print(f'[!] Exception: {e}')
    except KeyboardInterrupt:
        pass
