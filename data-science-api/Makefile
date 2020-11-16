setup:
	cp .env.example .env
	docker-compose -f docker-compose-test.yml build

up:
	docker-compose -f docker-compose-test.yml build
	docker-compose -f docker-compose-test.yml up -d processing-test

test:
	docker-compose -f docker-compose-test.yml down
	docker-compose -f docker-compose-test.yml build processing-test
	docker-compose -f docker-compose-test.yml run --rm \
		--service-ports processing-test python -m pytest tests -s -v

rm-containers:
	docker-compose stop
	docker-compose rm -f
	docker-compose -f docker-compose-test.yml stop
	docker-compose -f docker-compose-test.yml rm -f

documentation:
	docker-compose build
	docker-compose run --rm processing pdoc3 --force --html --output-dir /mnt/data/ api/
