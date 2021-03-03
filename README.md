# py-hdir
Helsedirektoratet test client in python3. Gives an overview of COVID-19 cases in Norway through an API provided by Helsedirektoratet. Requires a subscription key which you can get when you have registered as a data consumer (https://utvikler.helsedirektoratet.no/signup).

## Subscription key file
To make your secret subscription key file, use on OS X / Linux:
printf 'your-full-subscription-key' > key.secret

On Windows, use echo (not tested):
echo your-full-subscription-key > key.secret

The .gitignore should leave this file out of your commits.

## Output
In terminal, just a list over cases.

Vest 0007-0042-Helse-Fonna-HF
- 08-03-2020 0
- 09-03-2020 0
- 10-03-2020 0
- 11-03-2020 0
- 12-03-2020 0
- 13-03-2020 0
- 14-03-2020 0
- 15-03-2020 1
- 16-03-2020 1

## Licensing

This program is open source and free for everyone to use and modify.

For the underlying data access, please follow NLOD 2.0 (https://data.norge.no/nlod/en/2.0/) and the API provider (https://utvikler.helsedirektoratet.no/).