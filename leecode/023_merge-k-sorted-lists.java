package suanfa;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;

public class test2 {
	public static void main(String[] args) {
		ListNode ln1 = new ListNode(1);
		ListNode ln2 = new ListNode(4);
		ListNode ln3 = new ListNode(5);
		
		ListNode ln4 = new ListNode(1);
		ListNode ln5 = new ListNode(3);
		ListNode ln6 = new ListNode(4);
		
		ListNode ln7 = new ListNode(2);
		ListNode ln8 = new ListNode(6);
		
		ln1.next = ln2;
		ln2.next = ln3;

		ln4.next = ln5;
		ln5.next = ln6;

		ln7.next = ln8;
		
		ListNode[] lists = new ListNode[] {ln1, ln4, ln7};
		
//		System.out.println("mergeKLists");
//		List<Integer> ret = mergeKLists(lists);
//		for(int item: ret) {
//			System.out.print(item);
//		}
//		System.out.println();
		
		System.out.println("mergeKLists_2");
		ListNode ret2 = mergeKLists_2(lists);
		ListNode node = ret2;
		while(node.next != null) {
			node = node.next;
			System.out.print(node.val);
		}
		
	}
	
	public static List<Integer> mergeKLists(ListNode[] lists) {
	    //利用一个空的链表头方便插入节点。  
	    ListNode fakeHead = new ListNode(0), p = fakeHead;
	    int k = lists.length;
	  
	    
	    PriorityQueue<ListNode> heap = 
	        new PriorityQueue<ListNode>(k, new Comparator<ListNode>() {
	        	public int compare(ListNode a, ListNode b) {
	        		return a.val - b.val;
	        	}
	        });

	    // 从最小堆里将当前最小的节点取出，插入到结果链表中。
	    for (int i = 0; i < k; i++) {
	        if (lists[i] != null) {
	            heap.offer(lists[i]);
	        }
	    }

	    List<Integer> lst = new ArrayList<Integer>();
	    while (!heap.isEmpty()) {
	        ListNode node = heap.poll();
	        lst.add(node.val);
	        
	        p.next = node;
	        p = p.next;
	    
	        // 如果发现该节点后面还有后续节点，将后续节点加入到最小堆里。    
	        if (node.next != null) {
	            heap.offer(node.next);
	        }
	    }
	    
	    return lst;
		  
	}
	
	public static ListNode mergeKLists_2(ListNode[] lists) {
	    //利用一个空的链表头方便插入节点。  
	    ListNode fakeHead = new ListNode(0), p = fakeHead;
	    int k = lists.length;
	  
	    
	    PriorityQueue<ListNode> heap = 
	        new PriorityQueue<ListNode>(k, new Comparator<ListNode>() {
	        	public int compare(ListNode a, ListNode b) {
	        		return a.val - b.val;
	        	}
	        });

	    // 从最小堆里将当前最小的节点取出，插入到结果链表中。
	    for (int i = 0; i < k; i++) {
	        if (lists[i] != null) {
	            heap.offer(lists[i]);
	        }
	    }

	    List<Integer> lst = new ArrayList<Integer>();
	    while (!heap.isEmpty()) {
	        ListNode node = heap.poll();
	        lst.add(node.val);
	        
	        p.next = node;
	        p = p.next;
	    
	        // 如果发现该节点后面还有后续节点，将后续节点加入到最小堆里。    
	        if (node.next != null) {
	            heap.offer(node.next);
	        }
	    }
	    
	    return fakeHead;
	  
	}
}