class Node:
    
    def __init__(self, x: int, y: int):
        
        self.next = None
        self.header = None
        self.x = x
        self.y = y

class Header_Node:
    
    def __init__(self, Top = False):
        
        self.Top = Top
        self.size = 0
        self.first_node = None
        self.last_node = None
    
    def add_node(self, node: Node):
        
        if(self.size == 0):
            self.first_node = node
            self.last_node = node
            self.size = 1
            node.header = self
        else:
            self.last_node.next = node
            self.last_node = node
            node.header = self
            self.size += 1


class Solution:
    
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        
        #Merges head2 into head1 and returns head1
        def merge_headers(head1: Header_Node, head2: Header_Node) -> Header_Node:
            if(head1 == head2):
                return
            if(head2.Top):
                head1, head2 = head2, head1
            
            #Update headers of nodes in second list
            node_2 = head2.first_node
            while(node_2):
                node_2.header = head1
                header_dict[(node_2.x, node_2.y)] = head1
                node_2 = node_2.next
            if(head1.size == 0):
                head1.first_node = head2.first_node
                head1.last_node = head2.last_node
                head1.size = head2.size
            else:
                head1.last_node.next = head2.first_node
                head1.last_node = head2.last_node
                head1.size = head1.size + head2.size
            
            return head1
        
        def discover_node(x: int, y: int):
            
            grid[x][y] = 1
            New_Header = Header_Node()
            New_Node = Node(x,y)
            New_Header.add_node(New_Node)
            
            if(x + 1 < m and (x + 1, y) in header_dict.keys()):
                merge_headers(New_Node.header, header_dict[(x + 1, y)])

            if(x > 0 and (x - 1, y) in header_dict.keys()):
                merge_headers(New_Node.header, header_dict[(x - 1, y)])

            if(y + 1 < n and (x, y + 1) in header_dict.keys()):
                merge_headers(New_Node.header, header_dict[(x, y + 1)])

            if(y > 0 and (x, y - 1) in header_dict.keys()):
                merge_headers(New_Node.header, header_dict[(x, y - 1)])
            
            if(x == 0):
                merge_headers(New_Node.header, Top_Header)
            
            header_dict[(x,y)] = New_Node.header
        
        def process_hit(hit: List[int]) -> int:
            initial_top_size = Top_Header.size
            
            x = hit[0]
            y = hit[1]
            
            discover_node(x,y)

            final_top_size = Top_Header.size
            if(final_top_size == initial_top_size):
                return 0
            return final_top_size - initial_top_size - 1
        
        m = len(grid)
        n = len(grid[0])
        num_hits = len(hits)
        bad_hit_indices = set()
        
        for i in range(num_hits):
            if(grid[hits[i][0]][hits[i][1]]) == 1:
                grid[hits[i][0]][hits[i][1]] = 0
            else:
                bad_hit_indices.add(i)
                
            
        header_dict = {} #Maps a tuple (i,j) to header of node with coordinates (i,j)
        Top_Header = Header_Node(True)
        
        #Initiate Union-Find Structure
        for i in range(m):
            for j in range(n):
                if(grid[i][j] == 1):
                    discover_node(i,j)
                    
        
        ans = []
        index = len(hits) - 1
        while(index >= 0):
            if(index in bad_hit_indices):
                ans.append(0)
            else:
                ans.append(process_hit(hits[index]))
            index -= 1
        
        #Reverse ans
        final_ans = []
        l = len(ans)
        for i in range(l):
            final_ans.append(ans[l - 1 - i])
        return final_ans
