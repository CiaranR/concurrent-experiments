import eventlet

numbers = eventlet.queue.Queue()


@eventlet.spawn
def proc():
    x = numbers.get()
    y = numbers.get()
    z = numbers.get()
    return "%d + %d + %d = %d" % (x, y, z, x + y + z)

eventlet.spawn(numbers.put, 2 * 10)
eventlet.spawn(numbers.put, 2 * 20)
eventlet.spawn(numbers.put, 30 + 40)

print proc.wait()
