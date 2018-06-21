from ark.resource import Resource


class Statistics(Resource):

    def transactions(self, date_from, date_to):
        params = {
            'from': date_from.strftime('%s'),
            'to': date_to.strftime('%s')
        }
        return self.request_get('statistics/transactions', params)

    def blocks(self, date_from, date_to):
        params = {
            'from': date_from.strftime('%s'),
            'to': date_to.strftime('%s')
        }
        return self.request_get('statistics/blocks', params)

    def votes(self, date_from, date_to):
        params = {
            'from': date_from.strftime('%s'),
            'to': date_to.strftime('%s')
        }
        return self.request_get('statistics/votes', params)

    def unvotes(self, date_from, date_to):
        params = {
            'from': date_from.strftime('%s'),
            'to': date_to.strftime('%s')
        }
        return self.request_get('statistics/unvotes', params)
