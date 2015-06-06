from django.db import models


class HeatTemplate(models.Model):
    """
    Heat Template class, all values except description and name are required
    """
    name = models.CharField(name="Name", max_length=255)
    description = models.TextField(name="Description")
    default_flavor = models.CharField(name="Default flavor for VMs", blank=True)
    default_image = models.CharField(name="Default image for VMs", blank=True)
    default_private_network = models.UUIDField(blank=True)
    default_private_subnet = models.UUIDField(blank=True)
    default_public_network = models.UUIDField(blank=True)
    default_key = models.CharField(name="Default Keypair", blank=True)

    def __unicode__(self):
        return self.name


class SecurityGroup(models.Model):
    name = models.CharField(name="Name")

    def __unicode__(self):
        return self.name


class VM(models.Model):
    """
    Vm class, all values except description and name are required
    """
    template = models.ForeignKey(HeatTemplate)
    security_group = models.ForeignKey(SecurityGroup, blank=True)
    name = models.CharField(name="Name", max_length=255)
    description = models.TextField(name="Description")
    flavor = models.CharField(name="Flavor for VMs", blank=True)
    image = models.CharField(name="Image for VMs", blank=True)
    private_network = models.UUIDField(blank=True)
    private_subnet = models.UUIDField(blank=True)
    public_network = models.UUIDField(blank=True)
    key = models.CharField(name="Keypair", max_length=255)
    script = models.TextField(name="Deployment script")

    def __unicode__(self):
        return self.name


