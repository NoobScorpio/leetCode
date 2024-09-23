
//  Definition for singly-linked list.
function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var middleNode = function(head) {
    var end=head;
    var middle=head;
    while(end!=null && end.next!=null){
        end=end.next.next;
        middle=middle.next;
    }
    return middle;
};