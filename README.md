# python-project-euler

파이썬으로 [프로젝트 오일러](https://projecteuler.net/) 문제를 풀어보는 저장소입니다.

A repository for practicing [Project Euler](https://projecteuler.net/) problems with Python.

## 구조 / Structure

각 문제는 별도의 폴더에 구성됩니다.
Each problem is organized in its own folder.

```
problem_001/
    solution.py   ← 풀이 / solution
    test_solution.py  ← 테스트 / tests
```

## 실행 방법 / How to Run

### 의존성 설치 / Install Dependencies

```bash
pip install -r requirements.txt
```

### 테스트 실행 / Run Tests

```bash
pytest
```

### 특정 문제 테스트 / Run a Specific Problem

```bash
pytest problem_001/
```

## 문제 목록 / Problems

| 번호 / No. | 제목 / Title | 정답 / Answer |
|---|---|---|
| [001](problem_001/) | Multiples of 3 and 5 | 233168 |
| [002](problem_002/) | Even Fibonacci Numbers | 4613732 |
| [003](problem_003/) | Largest Prime Factor | 6857 |
| [004](problem_004/) | Largest Palindrome Product | 906609 |
| [005](problem_005/) | Smallest Multiple | 232792560 |
