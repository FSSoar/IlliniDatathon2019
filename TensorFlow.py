import tensorflow as tf
tf.reset_default_graph()
lstm_graph = tf.Graph()


class RNNConfig():
    input_size=1
    num_steps=30
    lstm_size=128
    num_layers=1
    keep_prob=0.8
    batch_size = 64
    init_learning_rate = 0.001
    learning_rate_decay = 0.99
    init_epoch = 5
    max_epoch = 50

config = RNNConfig()

with lstm_graph.as_default():
    inputs = tf.placeholder(tf.float32, [None, config.num_steps, config.input_size])
    targets = tf.placeholder(tf.float32, [None, config.input_size])
    learning_rate = tf.placeholder(tf.float32, None)

    def _create_one_cell():
        return tf.contrib.rnn.LSTMCell(config.lstm_size, state_is_tuple=True)
        if config.keep_prob < 1.0:
            return tf.contrib.rnn.DropoutWrapper(lstm_cell, output_keep_prob=config.keep_prob)

    cell = tf.contrib.rnn.MultiRNNCell(
        [_create_one_cell() for _ in range(config.num_layers)], 
        state_is_tuple=True
    ) if config.num_layers > 1 else _create_one_cell()

    val, _ = tf.nn.dynamic_rnn(cell, inputs, dtype=tf.float32)

    val = tf.transpose(val, [1, 0, 2])
    # last.get_shape() = (batch_size, lstm_size)
    last = tf.gather(val, int(val.get_shape()[0]) - 1, name="last_lstm_output")

    weight = tf.Variable(tf.truncated_normal([config.lstm_size, config.input_size]))
    bias = tf.Variable(tf.constant(0.1, shape=[config.input_size]))
    prediction = tf.matmul(last, weight) + bias

    loss = tf.reduce_mean(tf.square(prediction - targets))
    optimizer = tf.train.RMSPropOptimizer(learning_rate)
    minimize = optimizer.minimize(loss)


learning_rates_to_use = [
    config.init_learning_rate * (
        config.learning_rate_decay ** max(float(i + 1 - config.init_epoch), 0.0)
    ) for i in range(config.max_epoch)]

with tf.Session(graph=lstm_graph) as sess:

    tf.global_variables_initializer().run()
    for epoch_step in range(config.max_epoch):
        current_lr = learning_rates_to_use[epoch_step]
        
            # Check https://github.com/lilianweng/stock-rnn/blob/master/data_wrapper.py
            # if you are curious to know what is StockDataSet and how generate_one_epoch() 
            # is implemented.
        for batch_X, batch_y in stock_dataset.generate_one_epoch(config.batch_size):
            train_data_feed = {
                inputs: batch_X, 
                targets: batch_y, 
                learning_rate: current_lr
                }
            train_loss, _ = sess.run([loss, minimize], train_data_feed)

