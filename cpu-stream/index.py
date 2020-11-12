#!/usr/bin/python3
import controller.index

def main():
  route = controller.index.IndexController()
  route.indexAction()

if __name__ == '__main__':
  main()
