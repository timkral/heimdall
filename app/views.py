__author__ = 'tkral'

import json

from app import app
from flask import abort, request

@app.route('/commits/<commit_system>/<path:commit_path>/<commit_id>', methods=['GET', 'POST'])
def commit(commit_system, commit_path, commit_id):
    # Lookup plugin based on commit_system
    if request.method == 'GET':
        # commit_dict = plugin.load_commit_dict(commit_path, commit_id)
        commit_dict = {}
        commit_dict.update(category='commit')
        commit_dict.update(category_sub='{0}'.format(commit_system))
        commit_dict.update(commit_path='{0}'.format(commit_path))
        commit_dict.update(id='{0}'.format(commit_id))
        return json.dumps(commit_dict, sort_keys=True)
    else:
        # plugin.load_commit_dict(commit_path, commit_id)
        # push to db
        return '200'
