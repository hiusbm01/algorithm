#!/usr/bin/env python

import os
from urllib import parse

HEADER = """# 문제 풀이 목록

리포지토리에는 백준 및 프로그래머스 문제 풀이가 포함되어 있습니다.

## 목차
- [백준](#백준)
- [프로그래머스](#프로그래머스)

"""

FOOTER = """\n\n---\n자동 생성된 README입니다."""

def generate_readme():
    content = HEADER
    directories = []
    solveds = []

    for root, dirs, files in os.walk("."):
        dirs.sort()
        # 최상위 디렉토리 예외 처리
        if root == '.':
            for exclude_dir in ('.git', '.github', '__pycache__'):
                try:
                    dirs.remove(exclude_dir)
                except ValueError:
                    pass
            continue

        # 현재 디렉토리와 상위 디렉토리 정보
        category = os.path.basename(root)
        directory = os.path.basename(os.path.dirname(root))

        if category in ['백준', '프로그래머스'] and category not in directories:
            content += f"\n## {category}\n"
            directories.append(category)

        # 파일 리스트 정리
        for file in files:
            if file.endswith(('.md', '.java', '.py', '.cpp')) and category not in solveds:
                # 파일 경로 및 링크 생성
                file_path = os.path.join(root, file)
                link = parse.quote(file_path)
                content += f"- [{category}]({link})\n"
                solveds.append(category)

    content += FOOTER
    with open("README.md", "w", encoding="utf-8") as readme_file:
        readme_file.write(content)

if __name__ == "__main__":
    generate_readme()
