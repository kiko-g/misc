const randomRange = (min, max) => {
  if (typeof min !== "number" || typeof max !== "number") {
    throw new TypeError("Expected all arguments to be numbers")
  }

  return Math.min(min, max) + Math.random() * (Math.max(min, max) - Math.min(min, max))
}
