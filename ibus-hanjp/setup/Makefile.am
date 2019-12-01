setup_hanjp_PYTHON = \
	main.py \
	setup.ui \
	$(NULL)

nodist_setup_hanjp_PYTHON = config.py

setup_hanjpdir = $(datadir)/ibus-hanjp/setup

libexec_SCRIPTS = ibus-setup-hanjp

CLEANFILES = \
	*.pyc \
	$(NULL)

EXTRA_DIST = \
	ibus-setup-hanjp.in \
	$(NULL)

test:
	$(ENV) DBUS_DEBUG=true \
	       PYTHONPATH=$(abs_top_srcdir):$(pyexecdir) \
	       $(PYTHON) $(srcdir)/main.py

