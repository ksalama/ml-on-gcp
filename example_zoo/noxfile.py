# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import glob
import os

import nox


# Registered example sources to be tested.
SOURCES = ['tensorflow/probability']
 
# Each example is represented by its top-level directory.
EXAMPLES = []
for source in SOURCES:
	EXAMPLES.extend(glob.glob(os.path.join(source, '*')))


@nox.session(python='2.7')
@nox.parametrize('example', EXAMPLES)
def example_zoo_tests(session, example):
    session.install('pytest', 'google-cloud-storage')

    session.chdir(example)
    session.run('pytest', '-x')
