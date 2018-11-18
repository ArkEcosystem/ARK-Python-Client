from client.exceptions import ArkParameterException
from client.resource import Resource


class Blocks(Resource):

    def get(self, block_id):
        return self.request_get('blocks/get', {'id': block_id})

    def all(self, limit=20, offset=None, **kwargs):
        if limit > 100:
            raise ArkParameterException('Maximum number of objects to return is 100')
        extra_params = {name: kwargs[name] for name in kwargs if kwargs[name] is not None}
        params = {
            'limit': limit,
            'offset': offset,
            **extra_params
        }
        return self.request_get('blocks', params)

    def epoch(self):
        return self.request_get('blocks/getEpoch')

    def height(self):
        return self.request_get('blocks/getHeight')

    def nethash(self):
        return self.request_get('blocks/getNethash')

    def fee(self):
        return self.request_get('blocks/getFee')

    def fees(self):
        return self.request_get('blocks/getFees')

    def milestone(self):
        return self.request_get('blocks/getMilestone')

    def reward(self):
        return self.request_get('blocks/getReward')

    def supply(self):
        return self.request_get('blocks/getSupply')

    def status(self):
        return self.request_get('blocks/getStatus')
