### Demo using scriptedforms

#### Author: Fu-Chun Hsu, Infoready

Using the slider, string text,  and live sections combined with matplotlib plots you can
produce utilities like the following:

<section-start onLoad>

```python
t = np.linspace(-2*np.pi, 2*np.pi, 500)
omega = np.ones(3)

place = ""
name = ""
supervisor = ""
```

</section-start>

<section-live>
## What is your name:
<variable-string>name</variable-string>
```python
print('The name input is {}!'.format(name))
```
## Where do you work at today:
<variable-string>place</variable-string>

```python
print('The place work today is {}!'.format(place))
```
## What is your supervisor:
<variable-string>supervisor</variable-string>

```python
print('Your supervisor is {}'.format(supervisor))
```


# Lets see other examples


Angular frequencies ($\omega$):

<variable-slider label="$\omega [0]$" min="0" max="6" step="0.1">omega[0]</variable-slider>
<variable-slider label="$\omega [1]$" min="0" max="6" step="0.1">omega[1]</variable-slider>
<variable-slider label="$\omega [2]$" min="0" max="6" step="0.1">omega[2]</variable-slider>
```python
plt.figure(figsize=(5*1.618,5))

oscillation = np.sin(t[:, np.newaxis] * omega[np.newaxis, :])
summation = np.sum(oscillation, axis=1)

plt.plot(t, oscillation)
plt.plot(t, summation)

plt.xlim([-2*np.pi, 2*np.pi])
plt.ylim([-2.4, 2.4])
#plt.title('Two sin curves and their summation')
plt.title('Three sin curves and their summation')
plt.legend([
    r'$\omega [0] = {0:0.1f}$'.format(omega[0]),
    r'$\omega [1] = {0:0.1f}$'.format(omega[1]),
    r'$\omega [2] = {0:0.1f}$'.format(omega[2]),
    'Summation'], loc='upper right')
plt.xlabel('time (seconds)')
plt.ylabel(r'$sin(\omega \times t)$');
```

</section-live>