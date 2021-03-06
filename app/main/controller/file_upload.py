"""
@author Jacob Xie
@time 9/3/2020
"""

from flask_restx import Resource, Namespace, reqparse, abort
from werkzeug.datastructures import FileStorage
import pandas as pd

ns = Namespace("upload", description="Upload Excel and return spreadsheet")

xlsx_file = "xlsx_file"
xlsx_file_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
parser = reqparse.RequestParser()
parser.add_argument(xlsx_file,
                    type=FileStorage,
                    location="files")
param_head, param_multi_sheets = "head", "multiSheets"
parser.add_argument(param_head,
                    type=str)
parser.add_argument(param_multi_sheets,
                    type=str)


@ns.route("/upload")
class FileUploadAPI(Resource):

    @ns.expect(parser)
    def post(self):
        args = parser.parse_args()
        f = args.get(xlsx_file)

        hd = 0 if args.get(param_head) == "true" else None
        ms = None if args.get(param_multi_sheets) == "true" else 0
        if f is not None and f.content_type == xlsx_file_type:
            xs = pd.read_excel(f, header=hd, sheet_name=ms)
            if isinstance(xs, dict):
                res = {k: v.fillna("").to_dict(orient="records") for k, v in xs.items()}
            else:
                res = xs.fillna("").to_dict(orient="records")
            return res
        else:
            abort(404)
