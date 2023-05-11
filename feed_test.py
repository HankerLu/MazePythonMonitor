from enum import Enum
import numpy as np
# import matplotlib.pyplot as plt
print("aicutie feed text start")

class OperationType(Enum):
    ADD_TASK = 1
    MARK_TASK = 2
    BREAKDOWN_TASK = 3
    DELETE_TASK = 4
    RELIST_TASK = 5
    CREATE_LIST = 6
    EDIT_TASK = 7
    PLAN_TASK = 8
    NUM_OPERATION_TYPE = 9

operation_type_score_dict = [
    {'type': OperationType.ADD_TASK, 'score': 1},
    {'type': OperationType.MARK_TASK, 'score': 2},
    {'type': OperationType.BREAKDOWN_TASK, 'score': 2},
    {'type': OperationType.DELETE_TASK, 'score': -1},
    {'type': OperationType.RELIST_TASK, 'score': 0.5},
    {'type': OperationType.CREATE_LIST, 'score': 0.1},
    {'type': OperationType.EDIT_TASK, 'score': 0},
    {'type': OperationType.PLAN_TASK, 'score': 0.3},
]

final_output_array = []

# 生成10个0~OperationType.NUM_OPERATION_TYPE-1 以内的随机数
input_seq_array = np.random.randint(0, OperationType.NUM_OPERATION_TYPE.value, 10)
print("input_seq_array: ", input_seq_array)

total_score = 0
for i in range(0, len(input_seq_array)):
    # print("input_seq_array[", i, "]: ", input_seq_array[i])
    for j in range(0, len(operation_type_score_dict)):
        # print("operation_type_score_dict[", j, "]: ", operation_type_score_dict[j])
        if operation_type_score_dict[j]['type'].value == input_seq_array[i]:
            print("operation_type_score_dict[", j, "]['score']: ", operation_type_score_dict[j]['score'])
            total_score += operation_type_score_dict[j]['score']
            break

final_output_array.append(total_score)

print("total_score: ", total_score)

print(final_output_array)

