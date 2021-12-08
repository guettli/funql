# FunQL

# What is "FunQL"?

Something with PostgreSQL, so that everybody can enjoy power
of SQL.

# Install

```
python3 -m venv funql-env
cd funql-env/
. bin/activate
pip install -U pip wheel
pip install -e git+ssh://git@github.com/guettli/funql.git#egg=funql
cp src/funql/.env.example src/funql/.env
echo '. $VIRTUAL_ENV/src/funql/.env' >> bin/activate
echo 'export $(cut -d= -f1 $VIRTUAL_ENV/src/funql/.env)' >> bin/activate

. bin/activate

# You need to have PostgreSQL installed
# Create user "stoic_config" with password "stoic_config":
sudo runuser -u postgres -- createuser -s -P stoic_config

createdb $PGDATABASE
manage.py migrate
```

# Naming convention

See: https://github.com/guettli/django-htmx-fun

# Guidelines

See: https://github.com/guettli/programming-guidelines

