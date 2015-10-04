```python
import directadmin

api = directadmin.Api("admin", "password", "domain.com", 2222, https=True, cert=False)

print api.create_backup()
```
