class LinkedStackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedStack:
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        return self.top is None

    def get_top(self):
        if self.is_empty():
            return None
        return self.top.data

    def push(self, element):
        new_node = LinkedStackNode(element)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            print("栈已空，无法出栈")
            return None
        popped_data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return popped_data

    def display_from_top_to_bottom(self):
        if self.is_empty():
            print("栈为空")
            return
        current = self.top
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" ".join(elements))

    def display_from_bottom_to_top(self):
        if self.is_empty():
            print("栈为空")
            return
        current = self.top
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        elements.reverse()
        print(" ".join(map(str, elements)))

    def to_list_from_top(self):
        result = []
        current = self.top
        while current:
            result.append(current.data)
            current = current.next
        return result


stack = LinkedStack()

initial_elements = [12, 25, 33, 40, 56]
for element in initial_elements:
    stack.push(element)

print("初始链式栈创建完成，元素 [12, 25, 33, 40, 56] 依次入栈（56 为栈顶）")

print("\n1、判空与取栈顶：")
print(f"   栈是否为空：{stack.is_empty()}")
print(f"   栈顶元素：{stack.get_top()}")

print("\n2、入栈：")
stack.push(68)
print("   将元素 68 压入栈")
print("   更新后的链式栈（从栈顶到栈底）：", end="")
stack.display_from_top_to_bottom()

print("\n3、出栈：")
popped_element = stack.pop()
print(f"   被删除的栈顶元素：{popped_element}")
print("   更新后的链式栈（从栈顶到栈底）：", end="")
stack.display_from_top_to_bottom()

print("\n4、遍历输出：")
print("   从栈顶到栈底：", end="")
stack.display_from_top_to_bottom()
print("   从栈底到栈顶：", end="")
stack.display_from_bottom_to_top()
