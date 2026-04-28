from pathlib import Path
import configparser
import re

from setuptools import setup


MODULE_NAME = "z_health_healthprof_custom"
PACKAGE_NAME = f"trytond.modules.{MODULE_NAME}"
ROOT = Path(__file__).parent


def read_text(filename):
    return (ROOT / filename).read_text(encoding="utf-8")


config = configparser.ConfigParser()
config.read(ROOT / "tryton.cfg", encoding="utf-8")
info = dict(config.items("tryton"))

for key in ("depends", "extras_depend", "xml"):
    if key in info:
        info[key] = [line.strip() for line in info[key].strip().splitlines() if line.strip()]

version = info.get("version", "0.0.1")
tryton_version = info.get("tryton_version", version)
major_version, minor_version = map(int, tryton_version.split(".", 2)[:2])

requires = []

for dep in info.get("depends", []):
    if dep == "health":
        requires.append(f"gnuhealth == {version}")
    elif dep.startswith("health_"):
        health_package = dep.split("_", 1)[1]
        requires.append(f"gnuhealth_{health_package} == {version}")
    elif not re.match(r"(ir|res|webdav)(\W|$)", dep):
        requires.append(
            f"trytond_{dep} >= {major_version}.{minor_version}, "
            f"< {major_version}.{minor_version + 1}"
        )

requires.append(
    f"trytond >= {major_version}.{minor_version}, < {major_version}.{minor_version + 1}"
)

setup(
    name=f"trytond_{MODULE_NAME}",
    version=version,
    description="GNU Health customization for health professionals",
    long_description=read_text("README.md"),
    long_description_content_type="text/markdown",
    author="Local customization",
    url="https://www.gnuhealth.org",
    package_dir={PACKAGE_NAME: "."},
    packages=[PACKAGE_NAME],
    package_data={
        PACKAGE_NAME: info.get("xml", []) + ["tryton.cfg", "view/*.xml"],
    },
    include_package_data=True,
    classifiers=[
        "Environment :: Plugins",
        "Framework :: Tryton",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
    ],
    license="GPL-3",
    python_requires=">=3.10",
    install_requires=requires,
    zip_safe=False,
    entry_points=f"""
    [trytond.modules]
    {MODULE_NAME} = {PACKAGE_NAME}
    """,
)
