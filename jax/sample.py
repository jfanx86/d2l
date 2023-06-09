from jax import grad
import jax.numpy as jnp


def tanh(x):  # Define a function
  y = jnp.exp(-2.0 * x)
  return (1.0 - y) / (1.0 + y)


if __name__ == '__main__':
  grad_tanh = grad(tanh)  # Obtain its gradient function
  print(grad_tanh(1.0))  # Evaluate it at x = 1.0
