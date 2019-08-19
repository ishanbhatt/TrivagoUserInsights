from flask import request
from werkzeug.exceptions import BadRequest

from TrivagoApp import api, Resource, name_space, parser, argument_parser
from TrivagoApp import clicks_df


@name_space.route('/hotels')
class Amenities(Resource):

    @api.expect(parser)
    @api.doc(responses={200: 'OK', 400: 'Invalid / Inconsistent parameters'})
    def get(self):
        args = argument_parser.parse_arguments(request.args)
        # Get the latest ones only in case of more results as they are more relevant
        result = clicks_df.iloc[(clicks_df.index == args["user_id"])] \
                      .sort_values(by=0, ascending=False).iloc[:, 1].head(args["limit"]).tolist()

        if result:
            return {"hotels": result}
        else:
            raise BadRequest("Invalid user_id")

