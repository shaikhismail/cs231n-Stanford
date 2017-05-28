import numpy as np
import matplotlib.pyplot as plt


class TwoLayerNet(object):
  """
  A two-layer fully-connected neural network. The net has an input dimension of
  N, a hidden layer dimension of H, and performs classification over C classes.
  We train the network with a softmax loss function and L2 regularization on the
  weight matrices. The network uses a ReLU nonlinearity after the first fully
  connected layer.

  In other words, the network has the following architecture:

  input - fully connected layer - ReLU - fully connected layer - softmax

  The outputs of the second fully-connected layer are the scores for each class.
  """

  def __init__(self, input_size, hidden_size, output_size, std=1e-4):
    """
    Initialize the model. Weights are initialized to small random values and
    biases are initialized to zero. Weights and biases are stored in the
    variable self.params, which is a dictionary with the following keys:

    W1: First layer weights; has shape (D, H)
    b1: First layer biases; has shape (H,)
    W2: Second layer weights; has shape (H, C)
    b2: Second layer biases; has shape (C,)

    Inputs:
    - input_size: The dimension D of the input data.
    - hidden_size: The number of neurons H in the hidden layer.
    - output_size: The number of classes C.
    """
    self.params = {}
    self.params['W1'] = std * np.random.randn(input_size, hidden_size)
    self.params['b1'] = np.zeros(hidden_size)
    self.params['W2'] = std * np.random.randn(hidden_size, output_size)
    self.params['b2'] = np.zeros(output_size)

  def loss(self, X, y=None, reg=0.0):
    """
    Compute the loss and gradients for a two layer fully connected neural
    network.

    Inputs:
    - X: Input data of shape (N, D). Each X[i] is a training sample.
    - y: Vector of training labels. y[i] is the label for X[i], and each y[i] is
      an integer in the range 0 <= y[i] < C. This parameter is optional; if it
      is not passed then we only return scores, and if it is passed then we
      instead return the loss and gradients.
    - reg: Regularization strength.

    Returns:
    If y is None, return a matrix scores of shape (N, C) where scores[i, c] is
    the score for class c on input X[i].

    If y is not None, instead return a tuple of:
    - loss: Loss (data loss and regularization loss) for this batch of training
      samples.
    - grads: Dictionary mapping parameter names to gradients of those parameters
      with respect to the loss function; has the same keys as self.params.
    """
    # Unpack variables from the params dictionary
    W1, b1 = self.params['W1'], self.params['b1']
    W2, b2 = self.params['W2'], self.params['b2']
    N, D = X.shape
    #print b1.shape
    
    # Compute the forward pass
    num_train = X.shape[0]
    scores = None
    #b1 = np.tile(b1, (N, 1))
    #b2 = np.tile(b2, (N, 1))
    h1 = np.dot(X, W1) + b1              #(5,4)x(4,10) = (5,10)
    #print h1.shape
    h1[h1<0] = 0
    scores = np.dot(h1 ,W2)+ b2              #(5,10)x(10,3) = (5,3)
                             #(5,3)
    #############################################################################
    # TODO: Perform the forward pass, computing the class scores for the input. #
    # Store the result in the scores variable, which should be an array of      #
    # shape (N, C).                                                             #
    #############################################################################
    pass
    #############################################################################
    #                              END OF YOUR CODE                             #
    #############################################################################
    
    # If the targets are not given then jump out, we're done
    if y is None:
      return scores

    # Compute the loss
    loss = None
    #print 'y.shape = ' ,y.shape
    '''
    for i in range(scores.shape[0]):
        exp_scores = np.exp(scores[i])
        corr = exp_scores[y[i]]
        sum_exp = np.sum(exp_scores[i])
        prob = corr/sum_exp
        log_prob = -np.log(prob)
        loss += log_prob
    '''
    n = np.arange(N)
<<<<<<< HEAD
    #print 'scores before: ' ,scores
    scores -= np.amax(scores)
    #print 'scores later: ' ,scores
    exp_scores = np.exp(scores)
    #print 'exp_scores: ', exp_scores
    corr_scores = np.reshape(exp_scores[n,y],(exp_scores[n,y].shape[0],-1))
    #print 'corr_scores.shape :',corr_scores.shape 
=======
    scores -= np.amax(scores)
    exp_scores = np.exp(scores)
    corr_scores = np.reshape(exp_scores[n,y],(exp_scores[n,y].shape[0],-1))
>>>>>>> ae98b4adad7de60f992c774ba349387e64d29410
    sum_exp_scores = np.sum(exp_scores, axis = 1, keepdims = True)
    nlf = -np.log(corr_scores/sum_exp_scores)
    loss = np.sum(nlf)
    loss /= y.shape[0]
    loss += (np.sum(W1 * W1) + np.sum(W2 * W2)) * 0.5 * reg
    #############################################################################
    # TODO: Finish the forward pass, and compute the loss. This should include  #
    # both the data loss and L2 regularization for W1 and W2. Store the result  #
    # in the variable loss, which should be a scalar. Use the Softmax           #
    # classifier loss. So that your results match ours, multiply the            #
    # regularization loss by 0.5                                                #
    #############################################################################
    pass
    #############################################################################
    #                              END OF YOUR CODE                             #
    #############################################################################

    # Backward pass: compute gradients
    grads = {}
    dnlf = np.ones((N, 1))
    dsum_exp_scores = (sum_exp_scores/corr_scores) * (corr_scores/(sum_exp_scores**2)) * dnlf
    #print 'dsum_exp_scores.shape ' ,dsum_exp_scores.shape                                           #(5,1)
    dcorr_scores = -1*(sum_exp_scores/corr_scores) * (1/sum_exp_scores) * dnlf
    #print 'dcorr_scores.shape ' , dcorr_scores.shape
    dexp_scores = np.outer(dsum_exp_scores, np.ones(scores.shape[1]))
    dcorr_scores = np.reshape(dcorr_scores , (N,))
    dexp_scores[n,y] += dcorr_scores
    dscores = np.exp(scores) * dexp_scores
    dW2 = np.dot(h1.T, dscores)
    db2 = np.sum(dscores, axis = 0)
    dh1 = np.dot(dscores, W2.T)
<<<<<<< HEAD
    h1_like = np.ones(dh1.shape)
    h1_like[h1<0] = 0
    dh1 = dh1 * h1_like
=======
>>>>>>> ae98b4adad7de60f992c774ba349387e64d29410
    dW1 = np.dot(X.T, dh1)
    db1 = np.sum(dh1, axis = 0)
    #print 'db1 : ', db1
    grads['W1'] = dW1
    grads['W2'] = dW2
    grads['b1'] = db1
    grads['b2'] = db2
    #############################################################################
    # TODO: Compute the backward pass, computing the derivatives of the weights #
    # and biases. Store the results in the grads dictionary. For example,       #
    # grads['W1'] should store the gradient on W1, and be a matrix of same size #
    #############################################################################
    pass
    #############################################################################
    #                              END OF YOUR CODE                             #
    #############################################################################

    return loss, grads

  def train(self, X, y, X_val, y_val,
            learning_rate=1e-3, learning_rate_decay=0.95,
            reg=1e-5, num_iters=100,
            batch_size=200, verbose=False):
    """
    Train this neural network using stochastic gradient descent.

    Inputs:
    - X: A numpy array of shape (N, D) giving training data.
    - y: A numpy array f shape (N,) giving training labels; y[i] = c means that
      X[i] has label c, where 0 <= c < C.
    - X_val: A numpy array of shape (N_val, D) giving validation data.
    - y_val: A numpy array of shape (N_val,) giving validation labels.
    - learning_rate: Scalar giving learning rate for optimization.
    - learning_rate_decay: Scalar giving factor used to decay the learning rate
      after each epoch.
    - reg: Scalar giving regularization strength.
    - num_iters: Number of steps to take when optimizing.
    - batch_size: Number of training examples to use per step.
    - verbose: boolean; if true print progress during optimization.
    """
    num_train = X.shape[0]
    iterations_per_epoch = max(num_train / batch_size, 1)

    # Use SGD to optimize the parameters in self.model
    loss_history = []
    train_acc_history = []
    val_acc_history = []

    for it in xrange(num_iters):
      X_batch = None
      y_batch = None
      index = np.random.choice(num_train, batch_size, replace = True)
      X_batch = X[index]
      y_batch = y[index]
      #########################################################################
      # TODO: Create a random minibatch of training data and labels, storing  #
      # them in X_batch and y_batch respectively.                             #
      #########################################################################
      pass
      #########################################################################
      #                             END OF YOUR CODE                          #
      #########################################################################

      # Compute loss and gradients using the current minibatch
      loss, grads = self.loss(X_batch, y=y_batch, reg=reg)
      loss_history.append(loss)
      #print 'b1.shape = ',self.params['b1'].shape
      #print 'grads[b1].shape = ' , grads['b1'].shape
      self.params['W1'] -= learning_rate * grads['W1']
<<<<<<< HEAD
      self.params['b1']-= learning_rate * grads['b1']
      self.params['W2'] -= learning_rate * grads['W2']
      self.params['b2'] -= learning_rate * grads['b2']
=======
      self.params['b1'] = -(learning_rate * grads['b1'] - self.params['b1'])
      self.params['W2'] -= learning_rate * grads['W2']
      self.params['b2'] = -(learning_rate * grads['b2']-self.params['b2'])
>>>>>>> ae98b4adad7de60f992c774ba349387e64d29410
      #########################################################################
      # TODO: Use the gradients in the grads dictionary to update the         #
      # parameters of the network (stored in the dictionary self.params)      #
      # using stochastic gradient descent. You'll need to use the gradients   #
      # stored in the grads dictionary defined above.                         #
      #########################################################################
      pass
      #########################################################################
      #                             END OF YOUR CODE                          #
      #########################################################################

      if verbose and it % 100 == 0:
        print 'iteration %d / %d: loss %f' % (it, num_iters, loss)

      # Every epoch, check train and val accuracy and decay learning rate.
      if it % iterations_per_epoch == 0:
        # Check accuracy
        train_acc = (self.predict(X_batch) == y_batch).mean()
        val_acc = (self.predict(X_val) == y_val).mean()
        train_acc_history.append(train_acc)
        val_acc_history.append(val_acc)

        # Decay learning rate
        learning_rate *= learning_rate_decay

    return {
      'loss_history': loss_history,
      'train_acc_history': train_acc_history,
      'val_acc_history': val_acc_history,
    }

  def predict(self, X):
    """
    Use the trained weights of this two-layer network to predict labels for
    data points. For each data point we predict scores for each of the C
    classes, and assign each data point to the class with the highest score.

    Inputs:
    - X: A numpy array of shape (N, D) giving N D-dimensional data points to
      classify.

    Returns:
    - y_pred: A numpy array of shape (N,) giving predicted labels for each of
      the elements of X. For all i, y_pred[i] = c means that X[i] is predicted
      to have class c, where 0 <= c < C.
    """
    y_pred = None
    h1 = np.dot(X, self.params['W1']) + self.params['b1']  
    h1[h1<0] = 0
    scores = np.dot(h1 , self.params['W2'])+ self.params['b2']  
    y_pred = np.argmax(scores, axis = 1)
    
    ###########################################################################
    # TODO: Implement this function; it should be VERY simple!                #
    ###########################################################################
    pass
    ###########################################################################
    #                              END OF YOUR CODE                           #
    ###########################################################################

    return y_pred


    
