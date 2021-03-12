#!/bin/bash

echo "UT test start ..."
python3 -m unittest test_api.TestApi
echo "UT test end ..."