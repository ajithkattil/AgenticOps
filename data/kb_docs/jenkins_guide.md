# Jenkins Troubleshooting Guide

## NullPointerException
This is a common Java error. Make sure all variables are properly initialized before use.

## Kubernetes CrashLoopBackOff
This usually indicates repeated container failures. Run `kubectl describe pod` and `kubectl logs` to investigate.
