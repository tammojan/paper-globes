#!/usr/bin/env python


class Face(object):
    """         
    Face of a polyhedron, defined by its vertices. 
    
    Attributes
    ----------
    vertices: list
        list of Vertex objects confining the face
    ID: int
        number identifying the Face
    normal: tuple
        normal vector to the face
    origin: tuple
        origin of the local coordinate system
    """

    def __init__(self, vertices, ID):
        """
        Creates a Surface Object from a set of vertices
        
        Parameters
        ----------
        vertices: list
            list of Vertex objects confining the face
        ID: int
            number identifying the Face
        """
        
        self.vertices = vertices
        self.ID = ID
        
    def calNormal(self):
        """
        TO DO
        
        Calculates the normal vector to the Face
        """
        pass
    
    def pickOrigin(self):
        """
        TO DO
        
        Pick one of the vertices to be the origin of the local coordinate system
        """
        pass
    
    def calcAxes(self):
        """
        TO DO
        
        Calculates the axes of the local coordinate system
        """
        pass
    
    


class Vertex(object):

    def __init__(self, x, y, z, name):
        """
        Creates the Vertex Object with Carthesian coordinates
        
        Parameters
        ----------
        x: float
            x coordinate
        y: float
            y coordinate
        z: float
            z coordinate
        name: string
        
        Attributes
        ----------
        x: float
            x coordinate
        y: float
            y coordinate
        z: float
            z coordinate
        name: string
            single letter name
            for example, 'A'
        """
        
        self.x = x
        self.y = y
        self.z = z
        self.name = name

    def to_spherical(self):
        """
        Maybe we'll need it, who knows?
        :return:
        """
        pass

