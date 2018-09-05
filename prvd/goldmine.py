'''API client for the goldmine.provide.services microservice.'''

from api_client import APIClient

class Goldmine(APIClient):

    DEFAULT_HOST = 'goldmine.provide.services'

    def __init__(self, token):
        super(Goldmine, self).__init__(APIClient.DEFAULT_SCHEME, Goldmine.DEFAULT_HOST, token) 

    def fetch_bridges(self, params):
        return self.get('bridges', (self, params or {}))

    def fetch_bridge_details(self, bridge_id):
        return self.get('bridges/{}'.format(bridge_id), {})

    def create_bridge(self, params):
        return self.post('bridges', params)

    def fetch_connectors(self, params):
        return self.get('connectors', params)

    def fetch_connector_details(self, connectorId):
        return self.get('connectors/{}'.format(connectorId), {})

    def create_connector(self, params):
        return self.post('connectors', params)

    def delete_connector(self, connectorId):
        return self.delete('connectors/{}'.format(connectorId))

    def fetch_contracts(self, params):
        return self.get('contracts', params)

    def fetch_contract_details(self, contract_id):
        return self.get('contracts/{}'.format(contract_id), {})

    def create_contract(self, params):
        return self.post('contracts', params)

    def execute_contract(self, contract_id, params):
        return self.post('contracts/${contract_id}/execute', params)

    def fetch_networks(self, params):
        return self.get('networks', params)

    def create_network(self, params):
        return self.post('networks', params)

    def update_network(self, network_id, params):
        return self.put('networks/{}'.format(network_id), params)

    def fetch_network_details(self, network_id):
        return self.get('networks/{}'.format(network_id), {})

    def fetch_network_accounts(self, network_id, params):
        return self.get('networks/${network_id}/accounts', params)

    def fetch_network_blocks(self, network_id, params):
        return self.get('networks/${network_id}/blocks', params)

    def fetch_network_bridges(self, network_id, params):
        return self.get('networks/${network_id}/bridges', params)

    def fetch_network_connectors(self, network_id, params):
        return self.get('networks/${network_id}/connectors', params)

    def fetch_network_contracts(self, network_id, params):
        return self.get('networks/${network_id}/contracts', params)

    def fetch_network_contract_details(self, network_id, contract_id):
        return self.get('networks/{}/contracts/{}'.format(network_id, contract_id), {})

    def fetch_network_oracles(self, network_id, params):
        return self.get('networks/${network_id}/oracles', params)

    def fetch_network_tokens(self, network_id, params):
        return self.get('networks/${network_id}/tokens', params)

    def fetch_network_transactions(self, network_id, params):
        return self.get('networks/${network_id}/transactions', params)

    def fetch_network_transaction_details(self, network_id, transaction_id):
        return self.get('networks/{}/transactions/{}'.format(network_id, transaction_id), {})

    def fetch_network_status(self, network_id):
        return self.get('networks/${network_id}/status', {})

    def fetch_network_nodes(self, network_id, params):
        return self.get('networks/${network_id}/nodes', params)

    def create_network_node(self, network_id, params):
        return self.post('networks/${network_id}/nodes', params)

    def fetch_network_node_details(self, network_id, node_id):
        return self.get('networks/{}/nodes/{}'.format(network_id, node_id), {})

    def fetch_network_node_logs(self, network_id, node_id):
        return self.get('networks/{}/nodes/{}/logs'.format(network_id, node_id), {})

    def delete_network_node(self, network_id, node_id):
        return self.delete('networks/{}/nodes/{}'.format(network_id, node_id))

    def fetch_oracles(self, params):
        return self.get('oracles', params)

    def fetch_oracle_details(self, oracle_id):
        return self.get('oracles/{}'.format(oracle_id), {})

    def create_oracle(self, params):
        return self.post('oracles', params)

    def fetch_tokens(self, params):
        return self.get('tokens', params)

    def fetch_token_details(self, token_id):
        return self.get('tokens/{}'.format(token_id), {})

    def create_token(self, params):
        return self.post('tokens', params)

    def create_transaction(self, params):
        return self.post('transactions', params)

    def fetch_transactions(self, params):
        return self.get('transactions', params)

    def fetch_transaction_details(self, tx_id):
        return self.get('transactions/{}'.format(tx_id), {})

    def fetch_wallet_balance(self, wallet_id, token_id):
        return self.get('wallets/{}/balances/{}'.format(wallet_id, token_id), {})

    def fetch_wallets(self, params):
        return self.get('wallets', params)

    def fetch_wallet_details(self, wallet_id):
        return self.get('wallets/{}'.format(wallet_id), {})

    def create_wallet(self, params):
        return self.post('wallets', params)
