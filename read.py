import re
import csv
import os

# 正则表达式匹配时间、agent id 和 nodeid
log_pattern = re.compile(r'\[(.*?)\] planner INFO agent name: (.*?), loc:.*?id=(\d+)')

def parse_log_file(log_file_path):
    data = []
    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                match = log_pattern.search(line)
                if match:
                    time = match.group(1)
                    agent_id = match.group(2)
                    nodeid = match.group(3)
                    data.append([time, agent_id, nodeid])
                else:
                    print(f"未匹配的行: {line.strip()}")
    except FileNotFoundError:
        print(f"文件未找到: {log_file_path}")
    except Exception as e:
        print(f"发生错误: {e}")
    return data

def sort_data(data):
    # 按 time, agent id, nodeid 排序
    data.sort(key=lambda x: (x[0], x[1], x[2]))
    return data

def write_to_csv(data, output_file_path):
    try:
        with open(output_file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['time', 'agent id', 'nodeid'])
            writer.writerows(data)
        print(f"成功写入 CSV 文件: {output_file_path}")
    except Exception as e:
        print(f"写入 CSV 文件时发生错误: {e}")

def main():
    log_file_path = r"E:\vscode\planner_diff.log"  # 日志文件路径
    output_file_path = 'output.csv'  # 输出 CSV 文件路径

    # 检查日志文件是否存在
    if not os.path.exists(log_file_path):
        print(f"日志文件不存在: {log_file_path}")
        return

    print("开始解析日志文件...")
    data = parse_log_file(log_file_path)
    print(f"解析完成，共解析到 {len(data)} 条数据")

    print("开始排序数据...")
    sorted_data = sort_data(data)
    print("排序完成")

    print("开始写入 CSV 文件...")
    write_to_csv(sorted_data, output_file_path)

if __name__ == "__main__":
    main()