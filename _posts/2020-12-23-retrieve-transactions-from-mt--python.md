---
layout: post
title: How To Retrieve Transactions from Mint With Python
date: 2020-12-23 12:56
categories: how-to mint finance python
---

## Introduction ##

[Mint](http://mint.intuit.com) is a online interface that lets you link all of your bank accounts and credit cards 
to it and see all of your financial transactions at once.

I like to keep track my myspending, but right now that means downloading CSV files from about five different 
websites, importing them into Excel and classifying all of them manuall. 

If I could access the data on Mint and download it, I'd have all of my transactions in one place and I could 
categorize them and analyze them programmatically.

## Goal ##

My current goals are:
* Get all transaction data from Mint using a Python script
* Categorize the transactions into one of my budget categories
* Generate a budget analysis of my spending and remaining amount in each budget category

If I can run this script once a week or so I can get a report on my budget status and use that to direct my spending.

## Python Mint API ##

There's a Python API for Mint that can be found [here](https://github.com/mrooney/mintapi).

It relies on using a Chrome browswer to scrape data off of the site to gather your financial records.

### Installing the API ###

Run this at the command line:
{% highlight console %}
C:\Users\sfrie>pip install mintapi
Collecting mintapi
  Downloading https://files.pythonhosted.org/packages/42/1e/cd1e5803d565d3c379595254059289847da74eb4ddf01e6e144839f92343/mintapi-1.44.tar.gz
Collecting future (from mintapi)
  Downloading https://files.pythonhosted.org/packages/45/0b/38b06fd9b92dc2b68d58b75f900e97884c45bedd2ff83203d933cf5851c9/future-0.18.2.tar.gz (829kB)
     |████████████████████████████████| 829kB 6.8MB/s
Collecting mock (from mintapi)
  Downloading https://files.pythonhosted.org/packages/5c/03/b7e605db4a57c0f6fba744b11ef3ddf4ddebcada35022927a2b5fc623fdf/mock-4.0.3-py3-none-any.whl
Collecting requests (from mintapi)
  Downloading https://files.pythonhosted.org/packages/29/c1/24814557f1d22c56d50280771a17307e6bf87b70727d975fd6b2ce6b014a/requests-2.25.1-py2.py3-none-any.whl (61kB)
     |████████████████████████████████| 61kB 1.9MB/s
Collecting selenium-requests (from mintapi)
  Downloading https://files.pythonhosted.org/packages/78/72/94eadc1667bf4e17e1c5f880fdf8715144b22600114ee68266c8bdde3a09/selenium-requests-1.3.zip
Collecting xmltodict (from mintapi)
  Downloading https://files.pythonhosted.org/packages/28/fd/30d5c1d3ac29ce229f6bdc40bbc20b28f716e8b363140c26eff19122d8a5/xmltodict-0.12.0-py2.py3-none-any.whl
Collecting pandas>=1.0 (from mintapi)
  Downloading https://files.pythonhosted.org/packages/f4/b0/63aa0d048e4c3be3f0d2c3851cde44ce644bac3f527f9239df5ca15947d1/pandas-1.1.5-cp38-cp38-win32.whl (7.9MB)
     |████████████████████████████████| 7.9MB 6.4MB/s
Collecting selenium (from mintapi)
  Downloading https://files.pythonhosted.org/packages/80/d6/4294f0b4bce4de0abf13e17190289f9d0613b0a44e5dd6a7f5ca98459853/selenium-3.141.0-py2.py3-none-any.whl (904kB)
     |████████████████████████████████| 911kB ...
Collecting oathtool (from mintapi)
  Downloading https://files.pythonhosted.org/packages/75/cd/9d35865c9a581dd2c39598d07955b494e3cc704f3f2f6d2dd47f8dff78a5/oathtool-2.3.0-py3-none-any.whl
Collecting certifi>=2017.4.17 (from requests->mintapi)
  Downloading https://files.pythonhosted.org/packages/5e/a0/5f06e1e1d463903cf0c0eebeb751791119ed7a4b3737fdc9a77f1cdfb51f/certifi-2020.12.5-py2.py3-none-any.whl (147kB)
     |████████████████████████████████| 153kB 6.4MB/s
Collecting chardet<5,>=3.0.2 (from requests->mintapi)
  Downloading https://files.pythonhosted.org/packages/19/c7/fa589626997dd07bd87d9269342ccb74b1720384a4d739a1872bd84fbe68/chardet-4.0.0-py2.py3-none-any.whl (178kB)
     |████████████████████████████████| 184kB ...
Collecting idna<3,>=2.5 (from requests->mintapi)
  Downloading https://files.pythonhosted.org/packages/a2/38/928ddce2273eaa564f6f50de919327bf3a00f091b5baba8dfa9460f3a8a8/idna-2.10-py2.py3-none-any.whl (58kB)
     |████████████████████████████████| 61kB 4.1MB/s
Collecting urllib3<1.27,>=1.21.1 (from requests->mintapi)
  Downloading https://files.pythonhosted.org/packages/f5/71/45d36a8df68f3ebb098d6861b2c017f3d094538c0fb98fa61d4dc43e69b9/urllib3-1.26.2-py2.py3-none-any.whl (136kB)
     |████████████████████████████████| 143kB 6.4MB/s
Collecting six (from selenium-requests->mintapi)
  Downloading https://files.pythonhosted.org/packages/ee/ff/48bde5c0f013094d729fe4b0316ba2a24774b3ff1c52d924a8a4cb04078a/six-1.15.0-py2.py3-none-any.whl
Collecting tldextract (from selenium-requests->mintapi)
  Downloading https://files.pythonhosted.org/packages/7e/62/b6acd3129c5615b9860e670df07fd55b76175b63e6b7f68282c7cad38e9e/tldextract-3.1.0-py2.py3-none-any.whl (87kB)
     |████████████████████████████████| 92kB 5.8MB/s
Collecting numpy>=1.15.4 (from pandas>=1.0->mintapi)
  Downloading https://files.pythonhosted.org/packages/b1/a6/e570ac0fdc466491b2c5d54dc3373292de50b5a326f383909a6cfa224fbe/numpy-1.19.4-cp38-cp38-win32.whl (11.0MB)
     |████████████████████████████████| 11.0MB 6.4MB/s
Collecting pytz>=2017.2 (from pandas>=1.0->mintapi)
  Downloading https://files.pythonhosted.org/packages/12/f8/ff09af6ff61a3efaad5f61ba5facdf17e7722c4393f7d8a66674d2dbd29f/pytz-2020.4-py2.py3-none-any.whl (509kB)
     |████████████████████████████████| 512kB ...
Collecting python-dateutil>=2.7.3 (from pandas>=1.0->mintapi)
  Downloading https://files.pythonhosted.org/packages/d4/70/d60450c3dd48ef87586924207ae8907090de0b306af2bce5d134d78615cb/python_dateutil-2.8.1-py2.py3-none-any.whl (227kB)
     |████████████████████████████████| 235kB 6.8MB/s
Collecting importlib-resources; python_version < "3.9" (from oathtool->mintapi)
  Downloading https://files.pythonhosted.org/packages/8d/94/2f6ceee0c4e63bff0177c07e68d27c937a19f6bc77c4739755b49f5adb04/importlib_resources-3.3.1-py2.py3-none-any.whl
Collecting autocommand (from oathtool->mintapi)
  Downloading https://files.pythonhosted.org/packages/61/55/9fb7c5a63fe0a797054034ce9aeacded2ca078690c63413ebfa06c47ee56/autocommand-2.2.1-py3-none-any.whl
Collecting path (from oathtool->mintapi)
  Downloading https://files.pythonhosted.org/packages/ee/11/9f51c02c14cdd29383bd3a880d472a22629e090fbd1415075c979ff76d94/path-15.0.1-py3-none-any.whl
Collecting filelock>=3.0.8 (from tldextract->selenium-requests->mintapi)
  Downloading https://files.pythonhosted.org/packages/93/83/71a2ee6158bb9f39a90c0dea1637f81d5eef866e188e1971a1b1ab01a35a/filelock-3.0.12-py3-none-any.whl
Collecting requests-file>=1.4 (from tldextract->selenium-requests->mintapi)
  Downloading https://files.pythonhosted.org/packages/77/86/cdb5e8eaed90796aa83a6d9f75cfbd37af553c47a291cd47bc410ef9bdb2/requests_file-1.5.1-py2.py3-none-any.whl
Installing collected packages: future, mock, certifi, chardet, idna, urllib3, requests, selenium, six, filelock, requests-file, tldextract, selenium-requests, xmltodict, numpy, pytz, python-dateutil, pandas, importlib-resources, autocommand, path, oathtool, mintapi
  Running setup.py install for future ... done
  Running setup.py install for selenium-requests ... done
  Running setup.py install for mintapi ... done
Successfully installed autocommand-2.2.1 certifi-2020.12.5 chardet-4.0.0 filelock-3.0.12 future-0.18.2 idna-2.10 importlib-resources-3.3.1 mintapi-1.44 mock-4.0.3 numpy-1.19.4 oathtool-2.3.0 pandas-1.1.5 path-15.0.1 python-dateutil-2.8.1 pytz-2020.4 requests-2.25.1 requests-file-1.5.1 selenium-3.141.0 selenium-requests-1.3 six-1.15.0 tldextract-3.1.0 urllib3-1.26.2 xmltodict-0.12.0
{% endhighlight %}

That was successful.

The, to make sure it works, I try this:

{% highlight console %}

C:\Users\sfrie>python mintapi/api.py --keyring --headless sfriederichs@gmail.com
python: can't open file 'mintapi/api.py': [Errno 2] No such file or directory

{% endhighlight %}

Well, that must be somehwere else. Let's find it.

The file is located here: C:\Users\sfrie\AppData\Local\Programs\Python\Python38-32\Lib\site-packages

Let's navigate there and try again.

Here's another wrinkle:

{% highlight console %}

C:\Users\sfrie\AppData\Local\Programs\Python\Python38-32\Lib\site-packages>python mintapi/api.py --keyring --headless sfriederichs@gmail.com
usage: api.py [-h] [--session-path [SESSION_PATH]] [--accounts] [--budgets] [--budget_hist] [--net-worth]
              [--credit-score] [--credit-report] [--extended-accounts] [--transactions] [--extended-transactions]
              [--start-date [START_DATE]] [--include-investment] [--skip-duplicates] [--show-pending]
              [--filename FILENAME] [--keyring] [--headless] [--use-chromedriver-on-path]
              [--chromedriver-download-path CHROMEDRIVER_DOWNLOAD_PATH] [--mfa-method {sms,email,soft-token}]
              [--mfa-token MFA_TOKEN] [--imap-account IMAP_ACCOUNT] [--imap-password IMAP_PASSWORD]
              [--imap-server IMAP_SERVER] [--imap-folder IMAP_FOLDER] [--imap-test] [--no_wait_for_sync]
              [--wait_for_sync_timeout WAIT_FOR_SYNC_TIMEOUT] [--attention]
              [email] [password]
api.py: error: --keyring can only be used if the `keyring` library is installed.
{% endhighlight %}

Alright, does installing this do it?

{% highlight console %}
C:\Users\sfrie\AppData\Local\Programs\Python\Python38-32\Lib\site-packages>pip install keyring
Collecting keyring
  Downloading https://files.pythonhosted.org/packages/e2/23/c15f403d1993a003a711a37318bbe66096c0802b265047919d5c14a4d693/keyring-21.7.0-py3-none-any.whl
Collecting pywin32-ctypes!=0.1.0,!=0.1.1; sys_platform == "win32" (from keyring)
  Downloading https://files.pythonhosted.org/packages/9e/4b/3ab2720f1fa4b4bc924ef1932b842edf10007e4547ea8157b0b9fc78599a/pywin32_ctypes-0.2.0-py2.py3-none-any.whl
Installing collected packages: pywin32-ctypes, keyring
Successfully installed keyring-21.7.0 pywin32-ctypes-0.2.0
{% endhighlight %}

Now, here's what I did to test the script:

{% highlight console %}

 C:\Users\sfrie\AppData\Local\Programs\Python\Python38-32\Lib\site-packages>python mintapi/api.py --keyring --headless sfriederichs@gmail.com
Mint password:

DevTools listening on ws://127.0.0.1:59829/devtools/browser/9da9d1fd-bbdc-4dc3-be79-0f664fd73765
[1223/134828.031:INFO:CONSOLE(1)] "analytics performance metrics [object Object]", source: https://mint.intuit.com/handlebars/common_3.0.1170/common/cms/js/csa-init.js (1)
[1223/135927.928:INFO:CONSOLE(1)] "analytics performance metrics [object Object]", source: https://mint.intuit.com/handlebars/common_3.0.1170/common/cms/js/csa-init.js (1)
[1223/135927.934:INFO:CONSOLE(1)] "mtx-track-star.js has been loaded.", source: https://mint.intuit.com/handlebars/common/cms/js/track-star.js (1)

{% endhighlight %}

Well something happened anyway. I'll call it good.

### Basic Mint Script ###
Here's the suggsted basic script for Mint:

{% highlight python %}


 import mintapi
  mint = mintapi.Mint(
    'your_email@web.com',  # Email used to log in to Mint
    'password',  # Your password used to log in to mint
    # Optional parameters
    mfa_method='sms',  # Can be 'sms' (default), 'email', or 'soft-token'.
                       # if mintapi detects an MFA request, it will trigger the requested method
                       # and prompt on the command line.
    headless=False,  # Whether the chromedriver should work without opening a
                     # visible window (useful for server-side deployments)
    mfa_input_callback=None,  # A callback accepting a single argument (the prompt)
                              # which returns the user-inputted 2FA code. By default
                              # the default Python `input` function is used.
    session_path=None, # Directory that the Chrome persistent session will be written/read from.
                       # To avoid the 2FA code being asked for multiple times, you can either set
                       # this parameter or log in by hand in Chrome under the same user this runs
                       # as.
    imap_account=None, # account name used to log in to your IMAP server
    imap_password=None, # account password used to log in to your IMAP server
    imap_server=None,  # IMAP server host name
    imap_folder='INBOX',  # IMAP folder that receives MFA email
    wait_for_sync=False,  # do not wait for accounts to sync
    wait_for_sync_timeout=300,  # number of seconds to wait for sync
	use_chromedriver_on_path=False,  # True will use a system provided chromedriver binary that
	                                 # is on the PATH (instead of downloading the latest version)
  )

  # Get basic account information
  mint.get_accounts()

  # Get extended account detail at the expense of speed - requires an
  # additional API call for each account
  mint.get_accounts(True)

  # Get budget information
  mint.get_budgets()

  # Get transactions
  mint.get_transactions() # as pandas dataframe
  mint.get_transactions_csv(include_investment=False) # as raw csv data
  mint.get_transactions_json(include_investment=False, skip_duplicates=False)

  # Get transactions for a specific account
  accounts = mint.get_accounts(True)
  for account in accounts:
    mint.get_transactions_csv(id=account["id"])
    mint.get_transactions_json(id=account["id"])

  # Get net worth
  mint.get_net_worth()

  # Get credit score
  mint.get_credit_score()

  # Get bills
  mint.get_bills()

  # Get investments (holdings and transactions)
  mint.get_invests_json()

  # Close session and exit cleanly from selenium/chromedriver
  mint.close()

  # Initiate an account refresh
  mint.initiate_account_refresh()
{% endhighlight %}

So, this is what happens when I run it:

{% highlight console %}
C:\Users\sfrie\Dropbox\Projects\pyMint>python mintTest.py

DevTools listening on ws://127.0.0.1:60684/devtools/browser/4e663c4d-b730-4f39-b211-068829104a38
[32600:37920:1223/140751.559:ERROR:device_event_log_impl.cc(211)] [14:07:51.559] USB: usb_device_handle_win.cc:1020 Failed to read descriptor from node connection: A device attached to the system is not functioning. (0x1F)
[32600:37920:1223/140751.562:ERROR:device_event_log_impl.cc(211)] [14:07:51.561] USB: usb_device_handle_win.cc:1020 Failed to read descriptor from node connection: A device attached to the system is not functioning. (0x1F)
[32600:37920:1223/140751.567:ERROR:device_event_log_impl.cc(211)] [14:07:51.567] USB: usb_device_handle_win.cc:1020 Failed to read descriptor from node connection: A device attached to the system is not functioning. (0x1F)
[32600:37920:1223/140751.571:ERROR:device_event_log_impl.cc(211)] [14:07:51.570] USB: usb_device_handle_win.cc:1020 Failed to read descriptor from node connection: A device attached to the system is not functioning. (0x1F)
Traceback (most recent call last):
  File "mintTest.py", line 63, in <module>
    mint.get_transactions_csv(id=account["id"])
TypeError: get_transactions_csv() got an unexpected keyword argument 'id'
{% endhighlight %}

Hmm, that's interesting. I wonder if there's an API reference that I can use...

No, not a written one. I can look at the API code though. I see this:

{% highlight python %}
def get_transactions_csv(self, include_investment=False, acct=0):
{% endhighlight %}

So 'id' should probably be 'acct'.
However, the json version of this still uses 'id' so don't change that.

The get_credit_score function seems to have errors internally. I won't use it.

#### Getting Transactions as CSV ####

Okay, I'm using this script to grab the transactions:

{% highlight python %}
import mintapi
import csv
from io import StringIO

mint = mintapi.Mint(
'username',  # Email used to log in to Mint
'password',  # Your password used to log in to mint
# Optional parameters
mfa_method='sms',  # Can be 'sms' (default), 'email', or 'soft-token'.
                   # if mintapi detects an MFA request, it will trigger the requested method
                   # and prompt on the command line.
headless=True,  # Whether the chromedriver should work without opening a
                 # visible window (useful for server-side deployments)
mfa_input_callback=None,  # A callback accepting a single argument (the prompt)
                          # which returns the user-inputted 2FA code. By default
                          # the default Python `input` function is used.
session_path=None, # Directory that the Chrome persistent session will be written/read from.
                   # To avoid the 2FA code being asked for multiple times, you can either set
                   # this parameter or log in by hand in Chrome under the same user this runs
                   # as.
imap_account=None, # account name used to log in to your IMAP server
imap_password=None, # account password used to log in to your IMAP server
imap_server=None,  # IMAP server host name
imap_folder='INBOX',  # IMAP folder that receives MFA email
wait_for_sync=False,  # do not wait for accounts to sync
wait_for_sync_timeout=300,  # number of seconds to wait for sync
use_chromedriver_on_path=False,  # True will use a system provided chromedriver binary that
                                 # is on the PATH (instead of downloading the latest version)
)

# Get transactions
#mint.get_transactions() # as pandas dataframe
csvData = mint.get_transactions_csv(include_investment=False) # as raw csv data
csvDataHandle = StringIO(csvData.decode("utf-8"))

mint.close()

reader = csv.reader(csvDataHandle,delimiter = ',')

for date,desc,amount,transType,classification,account,burn1,burn2,burn3 in reader:
    print(str(date)+"\t"+str(desc) + "\t" + str(transType) + "\t" + str(classification) + "\t" +str(account) + "\t" + str(burn1) + "\t" + str(burn2) + "\t" + str(burn3))

{% endhighlight %}


## Resources ##


