from flask import request
from werkzeug.exceptions import BadRequest

from TrivagoApp import api, Resource, name_space, parser, argument_parser
from TrivagoApp import selection_df


@name_space.route('/amenities')
class Amenities(Resource):

    @api.expect(parser)
    @api.doc(responses={200: 'OK', 400: 'Invalid / Inconsistent parameters'})
    def get(self):
        args = argument_parser.parse_arguments(request.args)
        # Get the latest ones only in case of more results as they are more relevant
        result = selection_df.iloc[(selection_df.index == args["user_id"])] \
                    .sort_values(by=0, ascending=True).iloc[:, 1].head(args["limit"]).tolist()

        if result:
            return {"amenities": result}
        else:
            raise BadRequest("Invalid user_id")



