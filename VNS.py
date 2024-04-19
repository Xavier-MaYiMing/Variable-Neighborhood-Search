#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/4/8 19:55
# @Author  : Xavier Ma
# @Email   : xavier_mayiming@163.com
# @File    : VNS.py
# @Statement : The variable neighborhood search (VNS) for the traveling salesman problem (TSP).
# @Reference : Hansen P, Mladenović N. Variable neighborhood search: Principles and applications[J]. European Journal of Operational Research, 2001, 130(3): 449-467.
import numpy as np
import matplotlib.pyplot as plt


def cal_dis(dis_matrix, path):
    # calculate the length of the path
    path_shifted = np.roll(path, -1)
    return np.sum(dis_matrix[path, path_shifted])


def reversion(path, i, j):
    # the two-point reversion operation
    new_path = np.concatenate((path[:i], path[i: j + 1][::-1], path[j + 1:]))
    return new_path


def local_search(dis_matrix, path, operator):
    flag = True
    original_dis = cal_dis(dis_matrix, path)

    while flag:
        flag = False
        for i in range(1, len(path) - 1):
            for j in range(i + 1, len(path)):
                if j - i == 1:
                    continue
                new_path = operator(path, i, j)
                new_dis = cal_dis(dis_matrix, new_path)
                if new_dis < original_dis:
                    path = new_path
                    original_dis = new_dis
                    flag = True
    return path


def shaking(path, k):
    new_path = path.copy()
    for _ in range(k):
        [i, j] = sorted(np.random.choice(np.arange(1, len(path) - 1), 2, replace=False))
        new_path = reversion(new_path, i, j)
    return new_path


def main(coord_x, coord_y, k_max, operator=reversion):
    """
    The main function of the VNS.
    :param coord_x: x coordinate of the cities
    :param coord_y: y coordinate of the cities
    :param k_max: the maximum number of non-progressive iterations
    :param operator: the local search operation (default two-point reversion)
    :return:
    """
    # Step 1. Initialization
    num_cities = len(coord_x)
    dis_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities - 1):
        for j in range(i + 1, num_cities):
            dis_matrix[i, j] = dis_matrix[j, i] = np.sqrt(
                (coord_x[i] - coord_x[j]) ** 2 + (coord_y[i] - coord_y[j]) ** 2)
    k = 1
    path = np.random.permutation(num_cities)
    dis = cal_dis(dis_matrix, path)

    # Step 2. Optimization
    while k <= k_max:
        new_path = shaking(path, k)
        new_path = local_search(dis_matrix, new_path, operator)
        new_dis = cal_dis(dis_matrix, new_path)
        if new_dis < dis:
            dis = new_dis
            path = new_path
            k = 1
        else:
            k += 1

    # Step 3. Sort the results
    plt.figure()
    plt.scatter(coord_x, coord_y, color='black')
    for i in range(len(path) - 1):
        temp_x = [coord_x[path[i]], coord_x[path[i + 1]]]
        temp_y = [coord_y[path[i]], coord_y[path[i + 1]]]
        plt.plot(temp_x, temp_y, color='blue')
    temp_x = [coord_x[path[-1]], coord_x[path[0]]]
    temp_y = [coord_y[path[-1]], coord_y[path[0]]]
    plt.plot(temp_x, temp_y, color='blue')
    title = 'VNS for TSP'
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    # plt.savefig(title + '.png')
    plt.show()
    return 'best path: ' + str(path) + ', min distance: ' + str(dis)


if __name__ == '__main__':
    min_coord = 0
    max_coord = 10
    city_num = 50
    x = np.random.uniform(min_coord, max_coord, city_num)
    y = np.random.uniform(min_coord, max_coord, city_num)
    print(main(x, y, 100))
