# Copyright [2017] [Mauro Riva <lemariva@mail.com> <lemariva.com>]
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.


from setuptools import setup, find_packages
import optimize_upip

setup(name='captive-portal',
      version='0.0.1',
      description="""A captive portal framework for loading evil portals""",
      long_description=open('README.rst').read(),
      url='https://github.com/lemariva/uPyPortal',
      author='Mauro H. Riva',
      author_email='lemariva@gmail.com',
      license='Apache 2.0',
      cmdclass={'optimize_upip': optimize_upip.OptimizeUpip},
      packages=['captive_portal', 'captive_portal.templates'],
      install_requires=['picoweb', 'utemplate', 'micropython-logging',
                        'micropython-pkg_resources', 'micropython-btreedb'])
