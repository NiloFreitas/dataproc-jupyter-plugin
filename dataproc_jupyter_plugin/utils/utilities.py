# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
 
import json
import subprocess
from dataproc_jupyter_plugin.utils.constants import bq_public_dataset_project_id
 
class Utilities:
    def capture_shell_command_output(command):
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        if(result.returncode==0):
            output = result.stdout.strip()
        else:
            raise Exception(result.stderr.strip())
        return output
