# BlockChainSmokers
Using BlockChain to solve some of the problems in the voting process
# E-Voting
Any eligible voter can cast his/her vote via a computer device. The voting card will be fitted with a chip, if verified after being read by a card reader, the voter will be prompted to a Website. After signing into the website, the voter can see the list of candidates and vote for the desired candidate.
# Blockchain
The vote then will be stored on Azure's blockchain network.
# Accessibility
Any Voter can vote from anywhere in the nation from an ATM
# OutReach
The voters without any computer device or internet can vote on ATM-Like EVM set up by the ECI, The voting process will be similar to banking on an ATM, where the voter will insert his/her voting card and can click on the desired candidate after signing in.
# Use
Run the commands
run python manage.py runserver
then go to 127.0.0.1:8000/admin to create superusers and list of parties from a constituency and the respective political leaders.
python manage.py makemigrations accounts
python manage.py migrate accounts
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
