# syft absolute
import syft as sy
from syft.core.adp.ledger_store import DictLedgerStore
from syft.core.node.common.node_manager.dict_store import DictStore
from syft.core.node.common.node_service.simple.simple_messages import (
    NodeRunnableMessageWithReply,
)


def test_simple_service() -> None:
    d = sy.Domain("asdf", store_type=DictStore, ledger_store_type=DictLedgerStore)
    c = d.get_root_client()
    msg = NodeRunnableMessageWithReply("My Favourite")
    reply_msg = c.send_immediate_msg_with_reply(msg=msg)
    assert reply_msg.payload == "Nothing to see here...My Favourite"
