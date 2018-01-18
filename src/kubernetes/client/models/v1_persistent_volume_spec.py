# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.8.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1PersistentVolumeSpec(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'access_modes': 'list[str]',
        'aws_elastic_block_store': 'V1AWSElasticBlockStoreVolumeSource',
        'azure_disk': 'V1AzureDiskVolumeSource',
        'azure_file': 'V1AzureFilePersistentVolumeSource',
        'capacity': 'dict(str, str)',
        'cephfs': 'V1CephFSPersistentVolumeSource',
        'cinder': 'V1CinderVolumeSource',
        'claim_ref': 'V1ObjectReference',
        'fc': 'V1FCVolumeSource',
        'flex_volume': 'V1FlexVolumeSource',
        'flocker': 'V1FlockerVolumeSource',
        'gce_persistent_disk': 'V1GCEPersistentDiskVolumeSource',
        'glusterfs': 'V1GlusterfsVolumeSource',
        'host_path': 'V1HostPathVolumeSource',
        'iscsi': 'V1ISCSIVolumeSource',
        'local': 'V1LocalVolumeSource',
        'mount_options': 'list[str]',
        'nfs': 'V1NFSVolumeSource',
        'persistent_volume_reclaim_policy': 'str',
        'photon_persistent_disk': 'V1PhotonPersistentDiskVolumeSource',
        'portworx_volume': 'V1PortworxVolumeSource',
        'quobyte': 'V1QuobyteVolumeSource',
        'rbd': 'V1RBDVolumeSource',
        'scale_io': 'V1ScaleIOPersistentVolumeSource',
        'storage_class_name': 'str',
        'storageos': 'V1StorageOSPersistentVolumeSource',
        'vsphere_volume': 'V1VsphereVirtualDiskVolumeSource'
    }

    attribute_map = {
        'access_modes': 'accessModes',
        'aws_elastic_block_store': 'awsElasticBlockStore',
        'azure_disk': 'azureDisk',
        'azure_file': 'azureFile',
        'capacity': 'capacity',
        'cephfs': 'cephfs',
        'cinder': 'cinder',
        'claim_ref': 'claimRef',
        'fc': 'fc',
        'flex_volume': 'flexVolume',
        'flocker': 'flocker',
        'gce_persistent_disk': 'gcePersistentDisk',
        'glusterfs': 'glusterfs',
        'host_path': 'hostPath',
        'iscsi': 'iscsi',
        'local': 'local',
        'mount_options': 'mountOptions',
        'nfs': 'nfs',
        'persistent_volume_reclaim_policy': 'persistentVolumeReclaimPolicy',
        'photon_persistent_disk': 'photonPersistentDisk',
        'portworx_volume': 'portworxVolume',
        'quobyte': 'quobyte',
        'rbd': 'rbd',
        'scale_io': 'scaleIO',
        'storage_class_name': 'storageClassName',
        'storageos': 'storageos',
        'vsphere_volume': 'vsphereVolume'
    }

    def __init__(self, access_modes=None, aws_elastic_block_store=None, azure_disk=None, azure_file=None, capacity=None, cephfs=None, cinder=None, claim_ref=None, fc=None, flex_volume=None, flocker=None, gce_persistent_disk=None, glusterfs=None, host_path=None, iscsi=None, local=None, mount_options=None, nfs=None, persistent_volume_reclaim_policy=None, photon_persistent_disk=None, portworx_volume=None, quobyte=None, rbd=None, scale_io=None, storage_class_name=None, storageos=None, vsphere_volume=None):
        """
        V1PersistentVolumeSpec - a model defined in Swagger
        """

        self._access_modes = None
        self._aws_elastic_block_store = None
        self._azure_disk = None
        self._azure_file = None
        self._capacity = None
        self._cephfs = None
        self._cinder = None
        self._claim_ref = None
        self._fc = None
        self._flex_volume = None
        self._flocker = None
        self._gce_persistent_disk = None
        self._glusterfs = None
        self._host_path = None
        self._iscsi = None
        self._local = None
        self._mount_options = None
        self._nfs = None
        self._persistent_volume_reclaim_policy = None
        self._photon_persistent_disk = None
        self._portworx_volume = None
        self._quobyte = None
        self._rbd = None
        self._scale_io = None
        self._storage_class_name = None
        self._storageos = None
        self._vsphere_volume = None
        self.discriminator = None

        if access_modes is not None:
          self.access_modes = access_modes
        if aws_elastic_block_store is not None:
          self.aws_elastic_block_store = aws_elastic_block_store
        if azure_disk is not None:
          self.azure_disk = azure_disk
        if azure_file is not None:
          self.azure_file = azure_file
        if capacity is not None:
          self.capacity = capacity
        if cephfs is not None:
          self.cephfs = cephfs
        if cinder is not None:
          self.cinder = cinder
        if claim_ref is not None:
          self.claim_ref = claim_ref
        if fc is not None:
          self.fc = fc
        if flex_volume is not None:
          self.flex_volume = flex_volume
        if flocker is not None:
          self.flocker = flocker
        if gce_persistent_disk is not None:
          self.gce_persistent_disk = gce_persistent_disk
        if glusterfs is not None:
          self.glusterfs = glusterfs
        if host_path is not None:
          self.host_path = host_path
        if iscsi is not None:
          self.iscsi = iscsi
        if local is not None:
          self.local = local
        if mount_options is not None:
          self.mount_options = mount_options
        if nfs is not None:
          self.nfs = nfs
        if persistent_volume_reclaim_policy is not None:
          self.persistent_volume_reclaim_policy = persistent_volume_reclaim_policy
        if photon_persistent_disk is not None:
          self.photon_persistent_disk = photon_persistent_disk
        if portworx_volume is not None:
          self.portworx_volume = portworx_volume
        if quobyte is not None:
          self.quobyte = quobyte
        if rbd is not None:
          self.rbd = rbd
        if scale_io is not None:
          self.scale_io = scale_io
        if storage_class_name is not None:
          self.storage_class_name = storage_class_name
        if storageos is not None:
          self.storageos = storageos
        if vsphere_volume is not None:
          self.vsphere_volume = vsphere_volume

    @property
    def access_modes(self):
        """
        Gets the access_modes of this V1PersistentVolumeSpec.
        AccessModes contains all ways the volume can be mounted. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes

        :return: The access_modes of this V1PersistentVolumeSpec.
        :rtype: list[str]
        """
        return self._access_modes

    @access_modes.setter
    def access_modes(self, access_modes):
        """
        Sets the access_modes of this V1PersistentVolumeSpec.
        AccessModes contains all ways the volume can be mounted. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes

        :param access_modes: The access_modes of this V1PersistentVolumeSpec.
        :type: list[str]
        """

        self._access_modes = access_modes

    @property
    def aws_elastic_block_store(self):
        """
        Gets the aws_elastic_block_store of this V1PersistentVolumeSpec.
        AWSElasticBlockStore represents an AWS Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore

        :return: The aws_elastic_block_store of this V1PersistentVolumeSpec.
        :rtype: V1AWSElasticBlockStoreVolumeSource
        """
        return self._aws_elastic_block_store

    @aws_elastic_block_store.setter
    def aws_elastic_block_store(self, aws_elastic_block_store):
        """
        Sets the aws_elastic_block_store of this V1PersistentVolumeSpec.
        AWSElasticBlockStore represents an AWS Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore

        :param aws_elastic_block_store: The aws_elastic_block_store of this V1PersistentVolumeSpec.
        :type: V1AWSElasticBlockStoreVolumeSource
        """

        self._aws_elastic_block_store = aws_elastic_block_store

    @property
    def azure_disk(self):
        """
        Gets the azure_disk of this V1PersistentVolumeSpec.
        AzureDisk represents an Azure Data Disk mount on the host and bind mount to the pod.

        :return: The azure_disk of this V1PersistentVolumeSpec.
        :rtype: V1AzureDiskVolumeSource
        """
        return self._azure_disk

    @azure_disk.setter
    def azure_disk(self, azure_disk):
        """
        Sets the azure_disk of this V1PersistentVolumeSpec.
        AzureDisk represents an Azure Data Disk mount on the host and bind mount to the pod.

        :param azure_disk: The azure_disk of this V1PersistentVolumeSpec.
        :type: V1AzureDiskVolumeSource
        """

        self._azure_disk = azure_disk

    @property
    def azure_file(self):
        """
        Gets the azure_file of this V1PersistentVolumeSpec.
        AzureFile represents an Azure File Service mount on the host and bind mount to the pod.

        :return: The azure_file of this V1PersistentVolumeSpec.
        :rtype: V1AzureFilePersistentVolumeSource
        """
        return self._azure_file

    @azure_file.setter
    def azure_file(self, azure_file):
        """
        Sets the azure_file of this V1PersistentVolumeSpec.
        AzureFile represents an Azure File Service mount on the host and bind mount to the pod.

        :param azure_file: The azure_file of this V1PersistentVolumeSpec.
        :type: V1AzureFilePersistentVolumeSource
        """

        self._azure_file = azure_file

    @property
    def capacity(self):
        """
        Gets the capacity of this V1PersistentVolumeSpec.
        A description of the persistent volume's resources and capacity. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#capacity

        :return: The capacity of this V1PersistentVolumeSpec.
        :rtype: dict(str, str)
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """
        Sets the capacity of this V1PersistentVolumeSpec.
        A description of the persistent volume's resources and capacity. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#capacity

        :param capacity: The capacity of this V1PersistentVolumeSpec.
        :type: dict(str, str)
        """

        self._capacity = capacity

    @property
    def cephfs(self):
        """
        Gets the cephfs of this V1PersistentVolumeSpec.
        CephFS represents a Ceph FS mount on the host that shares a pod's lifetime

        :return: The cephfs of this V1PersistentVolumeSpec.
        :rtype: V1CephFSPersistentVolumeSource
        """
        return self._cephfs

    @cephfs.setter
    def cephfs(self, cephfs):
        """
        Sets the cephfs of this V1PersistentVolumeSpec.
        CephFS represents a Ceph FS mount on the host that shares a pod's lifetime

        :param cephfs: The cephfs of this V1PersistentVolumeSpec.
        :type: V1CephFSPersistentVolumeSource
        """

        self._cephfs = cephfs

    @property
    def cinder(self):
        """
        Gets the cinder of this V1PersistentVolumeSpec.
        Cinder represents a cinder volume attached and mounted on kubelets host machine More info: https://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md

        :return: The cinder of this V1PersistentVolumeSpec.
        :rtype: V1CinderVolumeSource
        """
        return self._cinder

    @cinder.setter
    def cinder(self, cinder):
        """
        Sets the cinder of this V1PersistentVolumeSpec.
        Cinder represents a cinder volume attached and mounted on kubelets host machine More info: https://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md

        :param cinder: The cinder of this V1PersistentVolumeSpec.
        :type: V1CinderVolumeSource
        """

        self._cinder = cinder

    @property
    def claim_ref(self):
        """
        Gets the claim_ref of this V1PersistentVolumeSpec.
        ClaimRef is part of a bi-directional binding between PersistentVolume and PersistentVolumeClaim. Expected to be non-nil when bound. claim.VolumeName is the authoritative bind between PV and PVC. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#binding

        :return: The claim_ref of this V1PersistentVolumeSpec.
        :rtype: V1ObjectReference
        """
        return self._claim_ref

    @claim_ref.setter
    def claim_ref(self, claim_ref):
        """
        Sets the claim_ref of this V1PersistentVolumeSpec.
        ClaimRef is part of a bi-directional binding between PersistentVolume and PersistentVolumeClaim. Expected to be non-nil when bound. claim.VolumeName is the authoritative bind between PV and PVC. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#binding

        :param claim_ref: The claim_ref of this V1PersistentVolumeSpec.
        :type: V1ObjectReference
        """

        self._claim_ref = claim_ref

    @property
    def fc(self):
        """
        Gets the fc of this V1PersistentVolumeSpec.
        FC represents a Fibre Channel resource that is attached to a kubelet's host machine and then exposed to the pod.

        :return: The fc of this V1PersistentVolumeSpec.
        :rtype: V1FCVolumeSource
        """
        return self._fc

    @fc.setter
    def fc(self, fc):
        """
        Sets the fc of this V1PersistentVolumeSpec.
        FC represents a Fibre Channel resource that is attached to a kubelet's host machine and then exposed to the pod.

        :param fc: The fc of this V1PersistentVolumeSpec.
        :type: V1FCVolumeSource
        """

        self._fc = fc

    @property
    def flex_volume(self):
        """
        Gets the flex_volume of this V1PersistentVolumeSpec.
        FlexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin. This is an alpha feature and may change in future.

        :return: The flex_volume of this V1PersistentVolumeSpec.
        :rtype: V1FlexVolumeSource
        """
        return self._flex_volume

    @flex_volume.setter
    def flex_volume(self, flex_volume):
        """
        Sets the flex_volume of this V1PersistentVolumeSpec.
        FlexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin. This is an alpha feature and may change in future.

        :param flex_volume: The flex_volume of this V1PersistentVolumeSpec.
        :type: V1FlexVolumeSource
        """

        self._flex_volume = flex_volume

    @property
    def flocker(self):
        """
        Gets the flocker of this V1PersistentVolumeSpec.
        Flocker represents a Flocker volume attached to a kubelet's host machine and exposed to the pod for its usage. This depends on the Flocker control service being running

        :return: The flocker of this V1PersistentVolumeSpec.
        :rtype: V1FlockerVolumeSource
        """
        return self._flocker

    @flocker.setter
    def flocker(self, flocker):
        """
        Sets the flocker of this V1PersistentVolumeSpec.
        Flocker represents a Flocker volume attached to a kubelet's host machine and exposed to the pod for its usage. This depends on the Flocker control service being running

        :param flocker: The flocker of this V1PersistentVolumeSpec.
        :type: V1FlockerVolumeSource
        """

        self._flocker = flocker

    @property
    def gce_persistent_disk(self):
        """
        Gets the gce_persistent_disk of this V1PersistentVolumeSpec.
        GCEPersistentDisk represents a GCE Disk resource that is attached to a kubelet's host machine and then exposed to the pod. Provisioned by an admin. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk

        :return: The gce_persistent_disk of this V1PersistentVolumeSpec.
        :rtype: V1GCEPersistentDiskVolumeSource
        """
        return self._gce_persistent_disk

    @gce_persistent_disk.setter
    def gce_persistent_disk(self, gce_persistent_disk):
        """
        Sets the gce_persistent_disk of this V1PersistentVolumeSpec.
        GCEPersistentDisk represents a GCE Disk resource that is attached to a kubelet's host machine and then exposed to the pod. Provisioned by an admin. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk

        :param gce_persistent_disk: The gce_persistent_disk of this V1PersistentVolumeSpec.
        :type: V1GCEPersistentDiskVolumeSource
        """

        self._gce_persistent_disk = gce_persistent_disk

    @property
    def glusterfs(self):
        """
        Gets the glusterfs of this V1PersistentVolumeSpec.
        Glusterfs represents a Glusterfs volume that is attached to a host and exposed to the pod. Provisioned by an admin. More info: https://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md

        :return: The glusterfs of this V1PersistentVolumeSpec.
        :rtype: V1GlusterfsVolumeSource
        """
        return self._glusterfs

    @glusterfs.setter
    def glusterfs(self, glusterfs):
        """
        Sets the glusterfs of this V1PersistentVolumeSpec.
        Glusterfs represents a Glusterfs volume that is attached to a host and exposed to the pod. Provisioned by an admin. More info: https://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md

        :param glusterfs: The glusterfs of this V1PersistentVolumeSpec.
        :type: V1GlusterfsVolumeSource
        """

        self._glusterfs = glusterfs

    @property
    def host_path(self):
        """
        Gets the host_path of this V1PersistentVolumeSpec.
        HostPath represents a directory on the host. Provisioned by a developer or tester. This is useful for single-node development and testing only! On-host storage is not supported in any way and WILL NOT WORK in a multi-node cluster. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath

        :return: The host_path of this V1PersistentVolumeSpec.
        :rtype: V1HostPathVolumeSource
        """
        return self._host_path

    @host_path.setter
    def host_path(self, host_path):
        """
        Sets the host_path of this V1PersistentVolumeSpec.
        HostPath represents a directory on the host. Provisioned by a developer or tester. This is useful for single-node development and testing only! On-host storage is not supported in any way and WILL NOT WORK in a multi-node cluster. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath

        :param host_path: The host_path of this V1PersistentVolumeSpec.
        :type: V1HostPathVolumeSource
        """

        self._host_path = host_path

    @property
    def iscsi(self):
        """
        Gets the iscsi of this V1PersistentVolumeSpec.
        ISCSI represents an ISCSI Disk resource that is attached to a kubelet's host machine and then exposed to the pod. Provisioned by an admin.

        :return: The iscsi of this V1PersistentVolumeSpec.
        :rtype: V1ISCSIVolumeSource
        """
        return self._iscsi

    @iscsi.setter
    def iscsi(self, iscsi):
        """
        Sets the iscsi of this V1PersistentVolumeSpec.
        ISCSI represents an ISCSI Disk resource that is attached to a kubelet's host machine and then exposed to the pod. Provisioned by an admin.

        :param iscsi: The iscsi of this V1PersistentVolumeSpec.
        :type: V1ISCSIVolumeSource
        """

        self._iscsi = iscsi

    @property
    def local(self):
        """
        Gets the local of this V1PersistentVolumeSpec.
        Local represents directly-attached storage with node affinity

        :return: The local of this V1PersistentVolumeSpec.
        :rtype: V1LocalVolumeSource
        """
        return self._local

    @local.setter
    def local(self, local):
        """
        Sets the local of this V1PersistentVolumeSpec.
        Local represents directly-attached storage with node affinity

        :param local: The local of this V1PersistentVolumeSpec.
        :type: V1LocalVolumeSource
        """

        self._local = local

    @property
    def mount_options(self):
        """
        Gets the mount_options of this V1PersistentVolumeSpec.
        A list of mount options, e.g. [\"ro\", \"soft\"]. Not validated - mount will simply fail if one is invalid. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#mount-options

        :return: The mount_options of this V1PersistentVolumeSpec.
        :rtype: list[str]
        """
        return self._mount_options

    @mount_options.setter
    def mount_options(self, mount_options):
        """
        Sets the mount_options of this V1PersistentVolumeSpec.
        A list of mount options, e.g. [\"ro\", \"soft\"]. Not validated - mount will simply fail if one is invalid. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#mount-options

        :param mount_options: The mount_options of this V1PersistentVolumeSpec.
        :type: list[str]
        """

        self._mount_options = mount_options

    @property
    def nfs(self):
        """
        Gets the nfs of this V1PersistentVolumeSpec.
        NFS represents an NFS mount on the host. Provisioned by an admin. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs

        :return: The nfs of this V1PersistentVolumeSpec.
        :rtype: V1NFSVolumeSource
        """
        return self._nfs

    @nfs.setter
    def nfs(self, nfs):
        """
        Sets the nfs of this V1PersistentVolumeSpec.
        NFS represents an NFS mount on the host. Provisioned by an admin. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs

        :param nfs: The nfs of this V1PersistentVolumeSpec.
        :type: V1NFSVolumeSource
        """

        self._nfs = nfs

    @property
    def persistent_volume_reclaim_policy(self):
        """
        Gets the persistent_volume_reclaim_policy of this V1PersistentVolumeSpec.
        What happens to a persistent volume when released from its claim. Valid options are Retain (default) and Recycle. Recycling must be supported by the volume plugin underlying this persistent volume. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#reclaiming

        :return: The persistent_volume_reclaim_policy of this V1PersistentVolumeSpec.
        :rtype: str
        """
        return self._persistent_volume_reclaim_policy

    @persistent_volume_reclaim_policy.setter
    def persistent_volume_reclaim_policy(self, persistent_volume_reclaim_policy):
        """
        Sets the persistent_volume_reclaim_policy of this V1PersistentVolumeSpec.
        What happens to a persistent volume when released from its claim. Valid options are Retain (default) and Recycle. Recycling must be supported by the volume plugin underlying this persistent volume. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#reclaiming

        :param persistent_volume_reclaim_policy: The persistent_volume_reclaim_policy of this V1PersistentVolumeSpec.
        :type: str
        """

        self._persistent_volume_reclaim_policy = persistent_volume_reclaim_policy

    @property
    def photon_persistent_disk(self):
        """
        Gets the photon_persistent_disk of this V1PersistentVolumeSpec.
        PhotonPersistentDisk represents a PhotonController persistent disk attached and mounted on kubelets host machine

        :return: The photon_persistent_disk of this V1PersistentVolumeSpec.
        :rtype: V1PhotonPersistentDiskVolumeSource
        """
        return self._photon_persistent_disk

    @photon_persistent_disk.setter
    def photon_persistent_disk(self, photon_persistent_disk):
        """
        Sets the photon_persistent_disk of this V1PersistentVolumeSpec.
        PhotonPersistentDisk represents a PhotonController persistent disk attached and mounted on kubelets host machine

        :param photon_persistent_disk: The photon_persistent_disk of this V1PersistentVolumeSpec.
        :type: V1PhotonPersistentDiskVolumeSource
        """

        self._photon_persistent_disk = photon_persistent_disk

    @property
    def portworx_volume(self):
        """
        Gets the portworx_volume of this V1PersistentVolumeSpec.
        PortworxVolume represents a portworx volume attached and mounted on kubelets host machine

        :return: The portworx_volume of this V1PersistentVolumeSpec.
        :rtype: V1PortworxVolumeSource
        """
        return self._portworx_volume

    @portworx_volume.setter
    def portworx_volume(self, portworx_volume):
        """
        Sets the portworx_volume of this V1PersistentVolumeSpec.
        PortworxVolume represents a portworx volume attached and mounted on kubelets host machine

        :param portworx_volume: The portworx_volume of this V1PersistentVolumeSpec.
        :type: V1PortworxVolumeSource
        """

        self._portworx_volume = portworx_volume

    @property
    def quobyte(self):
        """
        Gets the quobyte of this V1PersistentVolumeSpec.
        Quobyte represents a Quobyte mount on the host that shares a pod's lifetime

        :return: The quobyte of this V1PersistentVolumeSpec.
        :rtype: V1QuobyteVolumeSource
        """
        return self._quobyte

    @quobyte.setter
    def quobyte(self, quobyte):
        """
        Sets the quobyte of this V1PersistentVolumeSpec.
        Quobyte represents a Quobyte mount on the host that shares a pod's lifetime

        :param quobyte: The quobyte of this V1PersistentVolumeSpec.
        :type: V1QuobyteVolumeSource
        """

        self._quobyte = quobyte

    @property
    def rbd(self):
        """
        Gets the rbd of this V1PersistentVolumeSpec.
        RBD represents a Rados Block Device mount on the host that shares a pod's lifetime. More info: https://releases.k8s.io/HEAD/examples/volumes/rbd/README.md

        :return: The rbd of this V1PersistentVolumeSpec.
        :rtype: V1RBDVolumeSource
        """
        return self._rbd

    @rbd.setter
    def rbd(self, rbd):
        """
        Sets the rbd of this V1PersistentVolumeSpec.
        RBD represents a Rados Block Device mount on the host that shares a pod's lifetime. More info: https://releases.k8s.io/HEAD/examples/volumes/rbd/README.md

        :param rbd: The rbd of this V1PersistentVolumeSpec.
        :type: V1RBDVolumeSource
        """

        self._rbd = rbd

    @property
    def scale_io(self):
        """
        Gets the scale_io of this V1PersistentVolumeSpec.
        ScaleIO represents a ScaleIO persistent volume attached and mounted on Kubernetes nodes.

        :return: The scale_io of this V1PersistentVolumeSpec.
        :rtype: V1ScaleIOPersistentVolumeSource
        """
        return self._scale_io

    @scale_io.setter
    def scale_io(self, scale_io):
        """
        Sets the scale_io of this V1PersistentVolumeSpec.
        ScaleIO represents a ScaleIO persistent volume attached and mounted on Kubernetes nodes.

        :param scale_io: The scale_io of this V1PersistentVolumeSpec.
        :type: V1ScaleIOPersistentVolumeSource
        """

        self._scale_io = scale_io

    @property
    def storage_class_name(self):
        """
        Gets the storage_class_name of this V1PersistentVolumeSpec.
        Name of StorageClass to which this persistent volume belongs. Empty value means that this volume does not belong to any StorageClass.

        :return: The storage_class_name of this V1PersistentVolumeSpec.
        :rtype: str
        """
        return self._storage_class_name

    @storage_class_name.setter
    def storage_class_name(self, storage_class_name):
        """
        Sets the storage_class_name of this V1PersistentVolumeSpec.
        Name of StorageClass to which this persistent volume belongs. Empty value means that this volume does not belong to any StorageClass.

        :param storage_class_name: The storage_class_name of this V1PersistentVolumeSpec.
        :type: str
        """

        self._storage_class_name = storage_class_name

    @property
    def storageos(self):
        """
        Gets the storageos of this V1PersistentVolumeSpec.
        StorageOS represents a StorageOS volume that is attached to the kubelet's host machine and mounted into the pod More info: https://releases.k8s.io/HEAD/examples/volumes/storageos/README.md

        :return: The storageos of this V1PersistentVolumeSpec.
        :rtype: V1StorageOSPersistentVolumeSource
        """
        return self._storageos

    @storageos.setter
    def storageos(self, storageos):
        """
        Sets the storageos of this V1PersistentVolumeSpec.
        StorageOS represents a StorageOS volume that is attached to the kubelet's host machine and mounted into the pod More info: https://releases.k8s.io/HEAD/examples/volumes/storageos/README.md

        :param storageos: The storageos of this V1PersistentVolumeSpec.
        :type: V1StorageOSPersistentVolumeSource
        """

        self._storageos = storageos

    @property
    def vsphere_volume(self):
        """
        Gets the vsphere_volume of this V1PersistentVolumeSpec.
        VsphereVolume represents a vSphere volume attached and mounted on kubelets host machine

        :return: The vsphere_volume of this V1PersistentVolumeSpec.
        :rtype: V1VsphereVirtualDiskVolumeSource
        """
        return self._vsphere_volume

    @vsphere_volume.setter
    def vsphere_volume(self, vsphere_volume):
        """
        Sets the vsphere_volume of this V1PersistentVolumeSpec.
        VsphereVolume represents a vSphere volume attached and mounted on kubelets host machine

        :param vsphere_volume: The vsphere_volume of this V1PersistentVolumeSpec.
        :type: V1VsphereVirtualDiskVolumeSource
        """

        self._vsphere_volume = vsphere_volume

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1PersistentVolumeSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
