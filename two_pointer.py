#MERGED 2 SORTED LIST
def merge_lists(nums1, n, nums2, m):
  p1 = n - 1
  p2 = m - 1
  p = len(nums1) - 1

  while 0 <= p1 and 0 <= p2:
    if nums1[p1] < nums2[p2]:
      nums1[p] = nums2[p2]
      p2 -= 1
    else:
      nums1[p] = nums1[p1]
      p1 -= 1
    p -= 1
  # T = O( n + m ) = O( n )
  # S = O( 1 )

  if n != m:
    nums1[ : p2 + 1] = nums2[ : p2 + 1]

  return nums1

# Arrays de prueba 1
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
response = merge_lists(nums1, m, nums2, n)
print(response)

# Arrays de prueba 2
nums1 = [1,2,3,0,0,0,0]
m = 3
nums2 = [-4,2,3,9]
n = 4
response = merge_lists(nums1, m, nums2, n)
print(response)


#REORDER COLORS

def reorder_colors(colors:[int]):
    l = 0
    r = len(colors) - 1
    while(l < r):
        if colors[l] > colors[r]:
            colors[l], colors[r] = colors[r], colors[l]

        l += 1
    return colors

# Ejemplo 1:
nums = [2,0,2,1,1,0]
# Salida: [0,0,1,1,2,2]
result = reorder_colors(nums)
print(result)


# Ejemplo 2:
nums2 = [2,0,1]
# Salida: [0,1,2]
result2 = reorder_colors(nums2)
print(result2)
