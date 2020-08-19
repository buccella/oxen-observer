
# LMQ RPC endpoint of lokid; can be a unix socket 'ipc:///path/to/lokid.sock' (preferred) or a tcp
# socket 'tcp://127.0.0.1:5678'.  Typically you want this running with admin permission.
lokid_rpc = 'ipc://./devnet.sock'

# Default blocks per page for the index.
blocks_per_page=20
# Maximum blocks per page a user can request
max_blocks_per_page=100

# Some display and/or feature options:
pusher=True
key_image_checker=True
output_key_checker=True
autorefresh_option=True

# URLs to networks other than the one we are on:
mainnet_url='https://blocks.lokinet.dev'
testnet_url='https://testnet.lokinet.dev'
devnet_url='https://devnet.lokinet.dev'

# Same as above, but these apply if we are on a .loki URL:
lokinet_mainnet_url='http://kcpyawm9se7trdbzncimdi5t7st4p5mh9i1mg7gkpuubi4k4ku1y.loki'
lokinet_testnet_url='http://testnet.kcpyawm9se7trdbzncimdi5t7st4p5mh9i1mg7gkpuubi4k4ku1y.loki'
lokinet_devnet_url='http://devnet.kcpyawm9se7trdbzncimdi5t7st4p5mh9i1mg7gkpuubi4k4ku1y.loki'
